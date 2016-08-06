import pyglet
from .Constants import *
from .TextBox import TextBox
from .Jobs import *
from Game import Game

respond_rate = 1
window = pyglet.window.Window(256, 240)
game = Game()


def set_clear_color(color):
    pyglet.gl.gl.glClearColor(*color)
    window.clear()


@window.event
def on_draw():
    window.clear()