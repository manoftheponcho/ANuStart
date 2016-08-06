import pyglet


class Water:
    image_string = '{0}{0}{0}{1}{1}{0}{0}{0}' \
                   '{0}{0}{1}{1}{0}{0}{0}{0}' \
                   '{0}{0}{1}{0}{0}{0}{0}{0}' \
                   '{1}{1}{1}{0}{0}{0}{0}{0}' \
                   '{0}{0}{1}{1}{0}{0}{0}{0}' \
                   '{0}{0}{0}{1}{1}{1}{0}{0}' \
                   '{0}{0}{0}{1}{1}{1}{1}{1}' \
                   '{0}{0}{1}{1}{0}{0}{0}{1}'.format('\x64\xb0\xff\xff','\xc0\xdf\xff\xff')
    image = pyglet.image.create(8, 8)
    image.set_data('RGBA', 32, image_string)

if __name__ == "__main__":
    window = pyglet.window.Window(256, 240)
    tile = Water()

    @window.event
    def on_draw():
        window.clear()
        tile.image.blit(0, 0, 0)

    pyglet.app.run()
