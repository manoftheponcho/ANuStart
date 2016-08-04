import pyglet


class WhiteMage:
    job_name = "Wh.MAGE"

    def __init__(self):
        self.name = ''
        self.images = pyglet.resource.image('heroes.png')
        self.sprite = pyglet.sprite.Sprite(self.images.get_region(64, 0, 16, 24))
