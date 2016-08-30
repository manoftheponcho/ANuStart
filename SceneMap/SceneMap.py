import pyglet
import Engine
from Engine import BUTTON_START
from SceneMenu import SceneMenu
from SceneBattle import SceneBattle


class SceneMap:
    def __init__(self, current_map):
        self.map = current_map
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        for pos, tile in self.map.tiles.items():
            tile.image.blit(pos[0], pos[1], 0)
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        if symbol in BUTTON_START:
            SceneMenu()
        if symbol == pyglet.window.key.B:
            SceneBattle(self.map.formations[0])
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    import sys
    sys.path = sys.path[1:]  # dirty hack to get the importer to ignore this file (shame on me)
    from SceneMap import LimitedOverworld
    scene = SceneMap(LimitedOverworld())
    pyglet.app.run()
