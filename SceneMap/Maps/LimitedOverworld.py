import pyglet
from SceneMap.Tiles import Water, Grass, Mountain, Forest


class LimitedOverworld:
    tiles = [Water(x, 0) for x in range(0, 848, 16)]

if __name__ == "__main__":
    window = pyglet.window.Window(256, 240)
    current_map = LimitedOverworld()

    @window.event
    def on_draw():
        window.clear()
        for tile in current_map.tiles:
            tile.image.blit(tile.x, tile.y, 0)


    pyglet.app.run()