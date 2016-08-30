import pyglet
from .LightWarrior import LightWarrior


class BlackBelt(LightWarrior):
    job_name = "Bl.BELT"

    def __init__(self):
        super().__init__()
        # TODO: fix widths on image bytestrings
        self.image_string = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\xb0' \
                            b'\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\xb0' \
                            b'\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xffd\xb0\xff' \
                            b'\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd' \
                            b'\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\xb0' \
                            b'\xff\xffd\xb0\xff\xff\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff' \
                            b'\xffd\xb0\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xff' \
                            b'\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0' \
                            b'\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\xbc\xbe\x00\xffkm\x00\xffkm\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff\xbc\xbe\x00\xff\xbc' \
                            b'\xbe\x00\xff\xbc\xbe\x00\xffkm\x00\xffkm\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xffkm\x00' \
                            b'\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d' \
                            b'\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xffk' \
                            b'm\x00\xffkm\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xffkm\x00\xff\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\xb0\xff\xffd\xb0\xff\xff\xbc' \
                            b'\xbe\x00\xffd\xb0\xff\xff\xbc\xbe\x00\xffkm\x00\xffkm\x00\xff\xbc\xbe\x00\xff\xbc\xbe' \
                            b'\x00\xff\xbc\xbe\x00\xffkm\x00\xff\xbc\xbe\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffd\xb0' \
                            b'\xff\xffd\xb0\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xbc\xbe\x00\xffd\xb0\xff\xffd\xb0' \
                            b'\xff\xffd\xb0\xff\xffd\xb0\xff\xffkm\x00\xffkm\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff' \
                            b'\xbc\xbe\x00\xff\xbc\xbe\x00\xffkm\x00\xffd\xb0\xff\xffd\xb0\xff\xff\xbc\xbe\x00\xff' \
                            b'\xbc\xbe\x00\xff\x00\x00\x00\x00\xbc\xbe\x00\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xff' \
                            b'\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc' \
                            b'\xbe\x00\xffkm\x00\xffd\xb0\xff\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc' \
                            b'\xbe\x00\xff\x00\x00\x00\x00\xbc\xbe\x00\xffkm\x00\xffkm\x00\xffd\xb0\xff\xff\xbc\xbe' \
                            b'\x00\xff\xbc\xbe\x00\xff\x00\x00\x00\x00km\x00\xffkm\x00\xff\xbc\xbe\x00\xffd\xb0\xff' \
                            b'\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xff\xbc\xbe\x00\xffkm' \
                            b'\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffd\xb0\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbc\xbe\x00\xff\x00\x00' \
                            b'\x00\x00\xbc\xbe\x00\xff\xbc\xbe\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00' \
                            b'\xffkm\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00km\x00\xff\xbc\xbe\x00\xff\x00\x00\x00\x00\xbc\xbe\x00\xff\xbc\xbe\x00\xffkm' \
                            b'\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xff\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00km\x00\xffkm\x00\xff\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\xbc\xbe\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffk' \
                            b'm\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00km\x00\xffkm' \
                            b'\x00\xffd\xb0\xff\xffd\xb0\xff\xffd\xb0\xff\xffkm\x00\xffkm\x00\xffd\xb0\xff\xffd\xb0' \
                            b'\xff\xffd\xb0\xff\xffd\xb0\xff\xffkm\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00km\x00\xffkm\x00\xff\xbc\xbe\x00\xffkm\x00\xffkm\x00\xffkm\x00' \
                            b'\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xff\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00km\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm' \
                            b'\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xff\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00km\x00\xffkm' \
                            b'\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00' \
                            b'\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00km\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm' \
                            b'\x00\xffkm\x00\xffkm\x00\xffkm\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00km\x00' \
                            b'\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xffkm\x00\xff\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.image = pyglet.image.create(16, 24)
        self.image.set_data('RGBA', 64, self.image_string)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.exp_levels = [      0,     40,    196,    547,   1171,   2146,   3550,   5461,   7957,  11116,
                             15016,  19735,  25351,  31942,  39586,  48361,  58345,  69617,  82253,  96332,
                            111932, 129131, 148008, 168639, 191103, 215479, 241843, 270275, 300851, 333651,
                            366450, 399250, 432049, 464849, 497648, 530448, 563247, 596047, 628846, 661646,
                            694445, 727245, 760044, 792844, 825643, 858443, 891242, 924042, 956841, 989641]
        self.name = ''
        self.level = 1
        self.exp = 0
        self.max_hp = self.hp = 33
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.vitality = 20
        self.luck = 5
        self.accuracy = 5
        self.mdefense = 10


if __name__ == "__main__":
    window = pyglet.window.Window(256, 240)
    blackbelt = BlackBelt()

    @window.event
    def on_draw():
        window.clear()
        blackbelt.sprite.draw()
    pyglet.app.run()