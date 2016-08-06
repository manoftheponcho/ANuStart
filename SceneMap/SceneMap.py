import pyglet
import Engine


class SceneMap:
    def __init__(self):
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
