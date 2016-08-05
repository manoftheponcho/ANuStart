import pyglet
import Engine

class SceneWeaponMenu:
    def __init__(self):
        cursor_image = pyglet.resource.image('cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.fixed = pyglet.graphics.Batch()
        bg = pyglet.graphics.OrderedGroup(0)
        fg = pyglet.graphics.OrderedGroup(1)
        text = pyglet.graphics.OrderedGroup(2)
        self.objects = [Engine.TextBox(184, 48, 64,  8, batch=self.fixed, group=bg),
                        Engine.TextBox(184, 48, 64, 56, batch=self.fixed, group=bg),
                        Engine.TextBox(184, 48, 64,104, batch=self.fixed, group=bg),
                        Engine.TextBox(184, 48, 64,152, batch=self.fixed, group=bg),
                        Engine.TextBox(184, 32, 64,200, batch=self.fixed, group=bg),
                        Engine.TextBox( 64, 32,  8, 24, batch=self.fixed, group=fg),
                        Engine.TextBox( 64, 32,  8, 72, batch=self.fixed, group=fg),
                        Engine.TextBox( 64, 32,  8,120, batch=self.fixed, group=fg),
                        Engine.TextBox( 64, 32,  8,168, batch=self.fixed, group=fg),
                        Engine.TextBox( 56, 32,  8,200, batch=self.fixed, group=fg),
                        pyglet.text.Label('WEAPON', x=16, y=208, font_size=8, batch=self.fixed, group=text),
                        pyglet.text.Label('EQUIP',  x=88, y=208, font_size=8, batch=self.fixed, group=text),
                        pyglet.text.Label('TRADE', x=144, y=208, font_size=8, batch=self.fixed, group=text),
                        pyglet.text.Label('DROP',  x=200, y=208, font_size=8, batch=self.fixed, group=text)]
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        self.fixed.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        Engine.window.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneWeaponMenu()
    pyglet.app.run()