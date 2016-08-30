import pyglet
from .LightWarrior import LightWarrior


class BlackMage(LightWarrior):
    job_name = "Bl.MAGE"

    def __init__(self):
        super().__init__()
        self.name = ''
        self.images = pyglet.resource.image('heroes.png')
        self.sprite = pyglet.sprite.Sprite(self.images.get_region(80, 0, 16, 24))
        self.exp_levels = [     0,     40,    196,    547,   1171,   2146,   3550,   5461,   7957,  11116,
                            15016,  19735,  25351,  31942,  39586,  48361,  58345,  69617,  82253,  96332,
                           111932, 129131, 148008, 168639, 191103, 215479, 241843, 270275, 300851, 333651,
                           366450, 399250, 432049, 464849, 497648, 530448, 563247, 596047, 628846, 661646,
                           694445, 727245, 760044, 792844, 825643, 858443, 891242, 924042, 956841, 989641]
        self.max_hp = self.hp = 25
        self.level = 1
        self.exp = 0
        self.strength = 1
        self.agility = 10
        self.intelligence = 20
        self.vitality = 1
        self.luck = 10
        self.accuracy = 5
        self.mdefense = 20
