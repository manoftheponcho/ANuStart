import pyglet


class WhiteMage:
    job_name = "Wh.MAGE"

    def __init__(self):
        self.name = ''
        self.images = pyglet.resource.image('heroes.png')
        self.sprite = pyglet.sprite.Sprite(self.images.get_region(64, 0, 16, 24))
        self.exp_levels = [     0,     40,    196,    547,   1171,   2146,   3550,   5461,   7957,  11116,
                            15016,  19735,  25351,  31942,  39586,  48361,  58345,  69617,  82253,  96332,
                           111932, 129131, 148008, 168639, 191103, 215479, 241843, 270275, 300851, 333651,
                           366450, 399250, 432049, 464849, 497648, 530448, 563247, 596047, 628846, 661646,
                           694445, 727245, 760044, 792844, 825643, 858443, 891242, 924042, 956841, 989641]
        self.level = 1
        self.exp = 0
        self.max_hp = self.hp = 28
        self.strength = 5
        self.agility = 5
        self.intelligence = 15
        self.vitality = 10
        self.luck = 5
        self.accuracy = 5
        self.mdefense = 20
        self.attack = 2
        self.defense = 0
        self.evasion = 53


