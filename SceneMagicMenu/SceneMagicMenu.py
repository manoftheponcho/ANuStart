import pyglet
import Engine


class SceneMagicMenu:
    def __init__(self, index):
        cursor_image = pyglet.resource.image('cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.textboxes = [Engine.TextBox(240,152,  8, 64),
                          Engine.TextBox( 64, 32,  8,200)]
        self.labels = [pyglet.text.Label('{}'.format(index),   x=16, y=208, font_size=8)]
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        for box in self.textboxes:
            box.draw()
        for label in self.labels:
            label.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        Engine.window.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED  # the only keyboard event we want propagating up the stack

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneMagicMenu(0)
    pyglet.app.run()