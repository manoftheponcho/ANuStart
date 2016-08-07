import pyglet
from Engine.Constants import *
from Engine.TextBox import TextBox
from Engine.Jobs import *
from Game import Game

respond_rate = 1
window = pyglet.window.Window(512, 480)
game = Game()


def set_clear_color(color):
    pyglet.gl.gl.glClearColor(*color)
    window.clear()


def set_scale(x_scale, y_scale, z_scale):
    pyglet.gl.gl.glScalef(x_scale, y_scale, z_scale)
    window.clear()

@window.event
def on_draw():
    pyglet.gl.gl.glScalef(2.0, 2.0, 2.0)
