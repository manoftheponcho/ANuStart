import pyglet
from SceneMap.Tiles import Water, Grass, Mountain, Forest


class LimitedOverworld:
    tiles = [Water(x, 0) for x in range(0, 848, 16)] + \
            [Water(x, 16) for x in range(0, 848, 16)] + \
            [Water(x, 32) for x in range(0, 848, 16)] + \
            [Water(x, 48) for x in range(0, 848, 16)] + \
            [Water(x, 64) for x in range(0, 848, 16)] + \
            [Water(x, 80) for x in range(0, 848, 16)] + \
            [Water(x, 96) for x in range(0, 848, 16)] + \
            [Water(x, 112) for x in range(0, 528, 16)] + \
            [Grass(528, 112), Grass(544, 112)] + \
            [Water(x, 112) for x in range(560, 848, 16)] + \
            [Water(x, 128) for x in range(0, 528, 16)] + \
            [Grass(528, 128), Grass(544, 128), Grass(560, 128)] + \
            [Water(x, 128) for x in range(576, 848, 16)]

if __name__ == "__main__":
    window = pyglet.window.Window(1024, 960)
    current_map = LimitedOverworld()

    @window.event
    def on_draw():
        window.clear()
        for tile in current_map.tiles:
            tile.image.blit(tile.x, tile.y, 0)


    pyglet.app.run()