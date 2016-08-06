import Engine
import pyglet
from Engine import BLUE, UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B
from SceneJobSelect import SceneJobSelect

class SceneNewGame:
    def __init__(self):
        Engine.set_clear_color((0, 0, 0, 255))
        cursor_image = pyglet.resource.image('cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=72, y=135)
        self.textboxes = [Engine.TextBox(80, 32, 88, 128),
                          Engine.TextBox(80, 32, 88, 88),
                          Engine.TextBox(128, 32, 64, 48)]

        self.block = BLUE.create_image(120, 16)
        self.labels = [pyglet.text.Label('CONTINUE', x=96, y=136, font_size=8),
                       pyglet.text.Label('NEW GAME', x=96, y=96, font_size=8),
                       pyglet.text.Label('RESPOND RATE', x=72, y=56, font_size=8),
                       pyglet.text.Label('C 1987 SQUARE', x=64, y=32, font_size=8),
                       pyglet.text.Label('C 1990 NINTENDO', x=64, y=24, font_size=8)]
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        self.block.blit(64, 24, 0)
        for box in self.textboxes:
            box.draw()
        for label in self.labels:
            label.draw()
        self.cursor.draw()
        rr = Engine.respond_rate
        pyglet.text.Label('{}'.format(rr), x=176, y=56, font_size=8).draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        if symbol in UP or symbol in DOWN:
#            self.select_sound.play()
            self.cursor.y = 135 if self.cursor.y == 95 else 95
        elif symbol in LEFT:
#            self.move_sound.play()
            Engine.respond_rate = 8 if Engine.respond_rate == 1 else Engine.respond_rate - 1
        elif symbol in RIGHT:
#            self.move_sound.play()
            Engine.respond_rate = 1 if Engine.respond_rate == 8 else Engine.respond_rate + 1
        elif symbol in BUTTON_A:
            Engine.window.pop_handlers()
            SceneJobSelect()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneNewGame()
    pyglet.app.run()
