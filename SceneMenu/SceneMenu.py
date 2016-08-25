import sys, functools
import pyglet
import Engine
from Engine import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B
from SceneItemMenu import SceneItemMenu
from SceneMagicMenu import SceneMagicMenu
from SceneWeaponMenu import SceneWeaponMenu
from SceneArmorMenu import SceneArmorMenu
from SceneStatusMenu import SceneStatusMenu


class SceneMenu:
    def __init__(self):
        self.fixed = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.text = pyglet.graphics.OrderedGroup(1)
#        if sys.platform.startswith('linux'):
#            pyglet.options['audio'] = ('openal', 'pulse', 'silent')
#        self.menu_music = pyglet.media.load('./resources/menu.wav')
#        self.move_sound = pyglet.media.load('./resources/move.wav', streaming=False)
#        self.select_sound = pyglet.media.load('./resources/select.wav', streaming=False)
#        self.engine.play_music(self.menu_music)
        cursor_image = pyglet.resource.image('cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        Engine.game.heroes[0].sprite.x, Engine.game.heroes[0].sprite.y = (136, 191)
        Engine.game.heroes[1].sprite.x, Engine.game.heroes[1].sprite.y = (216, 191)
        Engine.game.heroes[2].sprite.x, Engine.game.heroes[2].sprite.y = (136,  79)
        Engine.game.heroes[3].sprite.x, Engine.game.heroes[3].sprite.y = (216,  79)
        self.objects = [Engine.TextBox(64, 64, 16,160, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80, 40,  8,120, batch=self.fixed, group=self.bg),
                        Engine.TextBox(64,112, 16,  8, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80,112, 88,  8, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80,112, 88,120, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80,112,168,  8, batch=self.fixed, group=self.bg),
                        Engine.TextBox(80,112,168,120, batch=self.fixed, group=self.bg)]
        HP_FORMAT = '{:3}/{:3}'
        GOLD_FORMAT = '{:6} G'
        LEVEL_FORMAT = 'L{:2}'
        self.labels = [pyglet.text.Label(Engine.game.heroes[0].name,
                                         x=96,  y=208, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(Engine.game.heroes[1].name,
                                         x=176, y=208, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(Engine.game.heroes[2].name,
                                         x=96,  y=96,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(Engine.game.heroes[3].name,
                                         x=176, y=96,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(Engine.game.heroes[0].hp, Engine.game.heroes[0].max_hp),
                                         x=96,  y=168, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(Engine.game.heroes[1].hp, Engine.game.heroes[1].max_hp),
                                         x=176, y=168, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(Engine.game.heroes[2].hp, Engine.game.heroes[2].max_hp),
                                         x=96,  y=56,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(Engine.game.heroes[3].hp, Engine.game.heroes[3].max_hp),
                                         x=176, y=56,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(GOLD_FORMAT.format(Engine.game.gold),
                                         x=16,  y=136, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(Engine.game.heroes[0].level),
                                         x=96,  y=192, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(Engine.game.heroes[1].level),
                                         x=176, y=192, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(Engine.game.heroes[2].level),
                                         x=96,  y=80,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(Engine.game.heroes[3].level),
                                         x=176, y=80,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('ITEM',   x=32, y=88, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('MAGIC',  x=32, y=72, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('WEAPON', x=32, y=56, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('ARMOR',  x=32, y=40, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('STATUS', x=32, y=24, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=96, y=176, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=176, y=176, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=96, y=64, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=176, y=64, font_size=8, batch=self.fixed, group=self.text)]
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.menu_select)

    def on_draw(self):
        Engine.window.clear()
        self.fixed.draw()
        for hero in Engine.game.heroes:
            hero.sprite.draw()
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def menu_select(self, symbol, modifiers):
        if symbol in UP:
#            self.move_sound.play()
            self.cursor.y = 15 if self.cursor.y == 79 else self.cursor.y + 16
        elif symbol in DOWN:
#            self.move_sound.play()
            self.cursor.y = 79 if self.cursor.y == 15 else self.cursor.y - 16
        elif symbol in BUTTON_A:
#            self.select_sound.play()
            if self.cursor.y == 79:  # ITEM
                SceneItemMenu()
            elif self.cursor.y == 63:  # MAGIC
                self.cursor.x, self.cursor.y = (72, 209)
                Engine.window.push_handlers(on_key_press=functools.partial(self.char_select, new_scene=SceneMagicMenu))
            elif self.cursor.y == 47:  # WEAPON
                SceneWeaponMenu()
            elif self.cursor.y == 31:  # ARMOR
                SceneArmorMenu()
            elif self.cursor.y == 15:  # STATUS
                self.cursor.x, self.cursor.y = (72, 209)
                Engine.window.push_handlers(on_key_press=functools.partial(self.char_select, new_scene=SceneStatusMenu))
        elif symbol in BUTTON_B:
            Engine.window.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

    def char_select(self, symbol, modifiers, new_scene):
        if symbol in UP + DOWN:
            self.cursor.y = {95: 209, 209: 95}[self.cursor.y]
        elif symbol in LEFT + RIGHT:
            self.cursor.x = {72: 152, 152: 72}[self.cursor.x]
        elif symbol in BUTTON_A:
            index = {(72,209):0, (152,209):1, (72,95):2, (152,95):3}[(self.cursor.x, self.cursor.y)]
            new_scene(index)
        elif symbol in BUTTON_B:
            self.cursor.x, self.cursor.y = (16,63)
            Engine.window.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneMenu()
    pyglet.app.run()
