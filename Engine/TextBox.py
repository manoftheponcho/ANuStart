import pyglet
from Engine.Constants import BLUE, GREY, WHITE


class TextBox(pyglet.sprite.Sprite):
#    corners = pyglet.resource.image("corners.png")
#    corners_seq = pyglet.image.ImageGrid(corners, 2, 2)

    def __init__(self, w, h, x=0, y=0, color=BLUE, batch=None, group=None):
        clamped_w = w if w > 16 else 16
        clamped_h = h if h > 16 else 16
        img = pyglet.image.Texture.create(clamped_w, clamped_h)
        img.blit_into(GREY.create_image(clamped_w - 2, clamped_h - 4), 1, 1, 0)
        img.blit_into(WHITE.create_image(clamped_w - 4, clamped_h - 7), 2, 3, 0)
        img.blit_into(GREY.create_image(clamped_w - 6, clamped_h - 9), 3, 4, 0)
#        img.blit_into(TextBox.corners_seq[0], 0, 0, 0)
#        img.blit_into(TextBox.corners_seq[1], clamped_w - 8, 0, 0)
#        img.blit_into(TextBox.corners_seq[2], 0, clamped_h - 8, 0)
#        img.blit_into(TextBox.corners_seq[3], clamped_w - 8, clamped_h - 8, 0)
        try:
            block = color.create_image(clamped_w - 10, clamped_h - 12)
        except AttributeError:
            block_color = pyglet.image.SolidColorImagePattern(color)
            block = block_color.create_image(clamped_w - 10, clamped_h - 12)
        img.blit_into(block, 5, 5, 0)
        super().__init__(img, x, y, batch=batch, group=group)
