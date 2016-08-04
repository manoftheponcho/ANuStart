import pyglet


class BlackMage:
    job_name = "Bl.MAGE"

    def __init__(self):
        self.name = ''
        self.images = pyglet.resource.image('heroes.png')
        self.sprite = pyglet.sprite.Sprite(self.images.get_region(80, 0, 16, 24))
