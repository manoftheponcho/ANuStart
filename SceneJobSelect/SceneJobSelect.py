import pyglet
import Engine
from SceneNameSelect import SceneNameSelect
from Engine import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B


class SceneJobSelect:

    def __init__(self):
        self.index_map = [(48, 159), (160, 159), (48, 63), (160, 63)]
        self.cycle = {Engine.Fighter: Engine.Thief, Engine.Thief: Engine.BlackBelt,
                      Engine.BlackBelt: Engine.RedMage, Engine.RedMage: Engine.WhiteMage,
                      Engine.WhiteMage: Engine.BlackMage, Engine.BlackMage: Engine.Fighter}
        Engine.game.heroes[0].sprite.x, Engine.game.heroes[0].sprite.y = (64, 151)
        Engine.game.heroes[1].sprite.x, Engine.game.heroes[1].sprite.y = (176, 151)
        Engine.game.heroes[2].sprite.x, Engine.game.heroes[2].sprite.y = (64, 55)
        Engine.game.heroes[3].sprite.x, Engine.game.heroes[3].sprite.y = (176, 55)
        self.index = 0
        self.fixed = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.text = pyglet.graphics.OrderedGroup(1)
        cursor_image = pyglet.resource.image('cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=48, y=159)
        self.objects = [Engine.TextBox(80, 80, 32, 32, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80, 80, 144, 32, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80, 80, 32, 128, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80, 80, 144, 128, batch=self.fixed, group=self.bg)]
        Engine.window.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        if self.index > 0 and Engine.game.heroes[self.index-1].name == '':
            self.index -= 1  # only place we can put a sanity check on SceneNameSelect's consequences
        self.fixed.draw()
        for hero in Engine.game.heroes:
            hero.sprite.draw()
        pyglet.text.Label(Engine.game.heroes[0].name, x=56, y=136, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[0].job_name, x=40, y=184, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[1].name, x=168, y=136, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[1].job_name, x=152, y=184, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[2].name, x=56, y=40, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[2].job_name, x=40, y=88, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[3].name, x=168, y=40, font_size=8).draw()
        pyglet.text.Label(Engine.game.heroes[3].job_name, x=152, y=88, font_size=8).draw()
        if self.index != 4:
            self.cursor.x, self.cursor.y = self.index_map[self.index]
            self.cursor.draw()
        return pyglet.event.EVENT_HANDLED  # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        if symbol in BUTTON_B:
            self.index = max(0, self.index-1)
        if self.index < 4:
            if symbol in UP + DOWN + LEFT + RIGHT:
                Engine.game.heroes[self.index] = self.cycle[type(Engine.game.heroes[self.index])]()
                Engine.game.heroes[self.index].sprite.x = self.cursor.x + 15
                Engine.game.heroes[self.index].sprite.y = self.cursor.y - 8
            elif symbol in BUTTON_A:
                self.index = min(4, self.index+1)
                SceneNameSelect(self.index-1)
        else:
            if symbol in BUTTON_A:
                Engine.window.pop_handlers()

        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneJobSelect()
    pyglet.app.run()