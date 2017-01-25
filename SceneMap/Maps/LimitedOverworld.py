import pyglet
import itertools
from SceneMap.Tiles import Water, Grass, Mountain, Forest
from SceneBattle import Formation, Imp, MadPony


class LimitedOverworld:
    tiles = {(x, y): Water() for x, y in itertools.product(range(0, 848, 16), range(0, 1104, 16))}
    tiles[(528, 112)], tiles[(544, 112)] = Grass(), Grass()
    formations = [Formation(Imp, Imp), Formation(MadPony)]

if __name__ == "__main__":
    window = pyglet.window.Window(1024, 960)
    current_map = LimitedOverworld()

    @window.event
    def on_draw():
        window.clear()
        for pos, tile in current_map.tiles.items():
            tile.image.blit(pos[0], pos[1], 0)


    pyglet.app.run()
