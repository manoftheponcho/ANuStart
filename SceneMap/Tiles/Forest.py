import pyglet


class Forest:
    image_string = ''.join(['{0}{1}{3}{1}{3}{3}{0}{1}{3}{0}{1}{3}{3}{0}{0}{3}',
                            '{1}{2}{1}{3}{3}{0}{3}{3}{3}{1}{3}{3}{3}{3}{3}{0}',
                            '{3}{3}{1}{3}{3}{0}{2}{3}{3}{1}{3}{3}{0}{0}{3}{3}',
                            '{0}{3}{3}{3}{0}{0}{2}{0}{0}{0}{0}{1}{1}{3}{1}{0}',
                            '{0}{3}{2}{3}{0}{0}{0}{3}{3}{0}{2}{3}{3}{3}{3}{3}',
                            '{0}{0}{1}{3}{3}{0}{0}{0}{0}{3}{3}{1}{3}{3}{3}{3}',
                            '{3}{0}{0}{3}{3}{1}{0}{3}{0}{1}{2}{3}{3}{3}{3}{3}',
                            '{3}{3}{3}{3}{0}{0}{3}{3}{0}{2}{3}{3}{3}{3}{3}{3}',
                            '{3}{0}{2}{0}{0}{0}{3}{3}{0}{0}{3}{0}{2}{3}{0}{3}',
                            '{0}{2}{3}{3}{3}{0}{0}{0}{0}{0}{0}{2}{3}{3}{0}{0}',
                            '{0}{2}{3}{3}{3}{0}{0}{3}{3}{0}{0}{2}{3}{3}{3}{3}',
                            '{0}{0}{2}{3}{3}{0}{0}{3}{0}{0}{0}{0}{3}{2}{3}{3}',
                            '{3}{0}{0}{0}{0}{0}{3}{0}{0}{0}{3}{0}{0}{0}{3}{0}',
                            '{3}{3}{0}{0}{1}{2}{0}{1}{2}{0}{0}{3}{3}{3}{0}{3}',
                            '{3}{0}{0}{3}{2}{3}{3}{3}{3}{3}{0}{0}{0}{0}{0}{3}',
                            '{3}{0}{0}{0}{0}{0}{3}{2}{3}{3}{0}{0}{0}{2}{2}{0}'][::-1])
    image_bytes = image_string.format('\x00\x00\x00\xff', '\x0d\x93\x00\xff', '\x88\xd8\x00\xff', '\x38\x87\x00\xff')
    image = pyglet.image.create(16, 16)
    image.set_data('RGBA', 64, image_bytes)

if __name__ == "__main__":
    window = pyglet.window.Window(256, 240)
    forest = Forest()

    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.gl.glScalef(12, 12, 12)
        Forest.image.blit(0, 0, 0)

    pyglet.app.run()