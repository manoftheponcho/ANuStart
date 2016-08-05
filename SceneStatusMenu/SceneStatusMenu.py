import pyglet
import Engine


class SceneStatusMenu:
    def __init__(self, index):
        next_level = [z for z in Engine.game.heroes[index].exp_levels if z > Engine.game.heroes[index].exp][0]
        self.fixed = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.text = pyglet.graphics.OrderedGroup(1)
        self.objects = [Engine.TextBox(112,104,  8,  8, batch=self.fixed, group=self.bg),
                        Engine.TextBox(112,104,120,  8, batch=self.fixed, group=self.bg),
                        Engine.TextBox(184, 56, 32,120, batch=self.fixed, group=self.bg),
                        Engine.TextBox( 64, 40,  8,176, batch=self.fixed, group=self.bg),
                        Engine.TextBox(112, 40, 72,176, batch=self.fixed, group=self.bg),
                        Engine.TextBox( 64, 40,184,176, batch=self.fixed, group=self.bg),
                        pyglet.text.Label('STR.', x=24, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].strength),
                                          x=88, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('AGL.', x=24, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].agility),
                                          x=88, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('INT.', x=24, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].intelligence),
                                          x=88, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('VIT.', x=24, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].vitality),
                                          x=88, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('LUCK', x=24, y=24, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].luck),
                                          x=88, y=24, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('DAMAGE', x=136, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].attack),
                                          x=200, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HIT %', x=136, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].accuracy),
                                          x=200, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('ABSORB', x=136, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].defense),
                                          x=200, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('EVADE %', x=136, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(Engine.game.heroes[index].evasion),
                                          x=200, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('EXP.POINTS', x=48, y=152, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:6}'.format(Engine.game.heroes[index].exp),
                                          x=160, y=152, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('FOR LEV UP', x=48, y=136, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:6}'.format(next_level - Engine.game.heroes[index].exp),
                                          x=160, y=136, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(Engine.game.heroes[index].name,
                                          x=16, y=192, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(Engine.game.heroes[index].job_name,
                                          x=120, y=192, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('LEV{:3}'.format(Engine.game.heroes[index].level),
                                          x=200, y=192, font_size=8, batch=self.fixed, group=self.text)]
        self.hero_sprite = pyglet.sprite.Sprite(Engine.game.heroes[index].image,
                                                x=88, y=184, batch=self.fixed, group=self.text)
        Engine.window.push_handlers(on_draw=self.on_draw,
                                    on_key_press=self.on_key_press)

    def on_draw(self):
        Engine.window.clear()
        self.fixed.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        Engine.window.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneStatusMenu(0)
    pyglet.app.run()