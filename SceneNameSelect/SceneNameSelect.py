import pyglet
import Engine


class SceneNameSelect:
    def __init__(self, index):
        self.index = index
        Engine.game.heroes[index].name = ''
        cursor_image = pyglet.resource.image('cursor.png')
        self.title = pyglet.text.Label('SELECT  NAME', x=72, y=24, font_size=8)
        self.name_box = Engine.TextBox(48, 32, 104, 192, Engine.RED)
        self.char_box = Engine.TextBox(184, 160, 32, 16)
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=32, y=143)
        self.chars = {
             (48, 152): 'A',  (64, 152): 'B',  (80, 152): 'C',  (96, 152): 'D', (112, 152): 'E',
            (128, 152): 'F', (144, 152): 'G', (160, 152): 'H', (176, 152): 'I', (192, 152): 'J',
             (48, 136): 'K',  (64, 136): 'L',  (80, 136): 'M',  (96, 136): 'N', (112, 136): 'O',
            (128, 136): 'P', (144, 136): 'Q', (160, 136): 'R', (176, 136): 'S', (192, 136): 'T',
             (48, 120): 'U',  (64, 120): 'V',  (80, 120): 'W',  (96, 120): 'X', (112, 120): 'Y',
            (128, 120): 'Z', (144, 120): "'", (160, 120): ',', (176, 120): '.', (192, 120): ' ',
             (48, 104): 'a',  (64, 104): 'b',  (80, 104): 'c',  (96, 104): 'd', (112, 104): 'e',
            (128, 104): 'f', (144, 104): 'g', (160, 104): 'h', (176, 104): 'i', (192, 104): 'j',
             (48,  88): 'k',  (64,  88): 'l',  (80,  88): 'm',  (96,  88): 'n', (112,  88): 'o',
            (128,  88): 'p', (144,  88): 'q', (160,  88): 'r', (176,  88): 's', (192,  88): 't',
             (48,  72): 'u',  (64,  72): 'v',  (80,  72): 'w',  (96,  72): 'x', (112,  72): 'y',
            (128,  72): 'z', (144,  72): '-', (160,  72): chr(0x2026), (176,  72): '!', (192,  72): '?'
                                                        # ellipsis
        }

        self.labels = [pyglet.text.Label(self.chars[key], x=key[0], y=key[1], font_size=8)
                       for key in self.chars.keys()]
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        self.name_box.draw()
        pyglet.text.Label(Engine.game.heroes[self.index].name, x=112, y=200, font_size=8).draw()
        self.char_box.draw()
        self.title.draw()
        for label in self.labels:
            label.draw()
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED  # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        if symbol in Engine.LEFT:
            self.cursor.x = 176 if self.cursor.x == 32 else self.cursor.x - 16
        elif symbol in Engine.RIGHT:
            self.cursor.x = 32 if self.cursor.x == 176 else self.cursor.x + 16
        if symbol in Engine.DOWN:
            self.cursor.y = 143 if self.cursor.y == 63 else self.cursor.y - 16
        elif symbol in Engine.UP:
            self.cursor.y = 63 if self.cursor.y == 143 else self.cursor.y + 16
        if symbol in Engine.BUTTON_A:
            if len(Engine.game.heroes[self.index].name) >= 4:
                Engine.window.pop_handlers()
            else:
                Engine.game.heroes[self.index].name += self.chars[(self.cursor.x + 16, self.cursor.y + 9)]
        elif symbol in Engine.BUTTON_B:
            if len(Engine.game.heroes[self.index].name) <= 0:
                Engine.window.pop_handlers()
            else:
                Engine.game.heroes[self.index].name = Engine.game.heroes[self.index].name[:-1]
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneNameSelect(0)
    pyglet.app.run()
