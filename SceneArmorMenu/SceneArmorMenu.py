import pyglet
import Engine


class SceneArmorMenu:
    def __init__(self):
        cursor_image = pyglet.resource.image('cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.textboxes = [Engine.TextBox(184, 48, 64,   8),
                          Engine.TextBox(184, 48, 64,  56),
                          Engine.TextBox(184, 48, 64, 104),
                          Engine.TextBox(184, 48, 64, 152),
                          Engine.TextBox(184, 32, 64, 200),
                          Engine.TextBox( 64, 32,  8,  24),
                          Engine.TextBox( 64, 32,  8,  72),
                          Engine.TextBox( 64, 32,  8, 120),
                          Engine.TextBox( 64, 32,  8, 168),
                          Engine.TextBox( 56, 32,  8, 200)]
        self.labels = [pyglet.text.Label('ARMOR',   x=16, y=208, font_size=8),
                       pyglet.text.Label('EQUIP', x=88, y=208, font_size=8),
                       pyglet.text.Label('TRADE', x=144, y=208, font_size=8),
                       pyglet.text.Label('DROP', x=200, y=208, font_size=8)]
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
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneArmorMenu()
    pyglet.app.run()
