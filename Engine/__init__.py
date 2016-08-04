import pyglet
from .Constants import *
from .TextBox import TextBox
from .Jobs import *

respond_rate = 1
window = pyglet.window.Window(256, 240)
objects = set()


def set_clear_color(color):
    pyglet.gl.gl.glClearColor(*color)
    window.clear()


def draw_text(text, pos=(0, 0), color=(255, 255, 255, 255)):
    objects.add(pyglet.text.Label(text, color=color, x=pos[0], y=pos[1], font_size=8))


@window.event
def on_draw():
    window.clear()
    for obj in objects:
        obj.draw()
