import pyglet

from SceneMap.Tiles import Water


class WaterMap:
    def __init__(self):
        self.tiles = [Water(0, 0), Water(16, 0)]


if __name__ == "__main__":
    window = pyglet.window.Window(256, 240)
    current_map = WaterMap()

    @window.event
    def on_draw():
        window.clear()
        for tile in current_map.tiles:
            tile.image.blit(tile.x, tile.y, 0)

    pyglet.app.run()