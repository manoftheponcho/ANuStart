__author__ = 'DUDE'

import pyglet
import random
import Engine
from Engine import LEFT, RIGHT, DOWN, UP, BUTTON_A, BUTTON_B, BLACK, TextBox

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()


class Battler(object):

    def __init__(self):
        super().__init__()
        self.status = set()
        self._hp = 1

    @property
    def incapacitated(self):
        if 'Dead' in self.status or 'Stone' in self.status:
            return True
        return False

    @property
    def unconscious(self):
        if self.incapacitated or 'Stun' in self.status or 'Sleep' in self.status:
            return True
        return False

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, other):
        self._hp = other
        self._hp = max(0, self._hp)
        if self._hp == 0:
            self.status.add('Dead')

class Enemy(Battler):
    images = pyglet.resource.image('monsters.png')
    def __init__(self):
        super().__init__()
        self.maxhp = self.hp = 1
        self.attack = 0
        self.accuracy = 0
        self.hits = 1
        self.crit = 0
        self.defense = 0
        self.evasion = 0
        self.mdefense = 0
        self.morale = 0
        self.statAttack = set()
        self.elemAttack = set()
        self.species = set()
        self.weak = set()
        self.resist = set()
        self.magic = []
        self.magic_chance = 0
        self.skills = []
        self.skill_chance = 0
        self.gold = 0
        self.exp = 0
        self.sprite = None

    def ai_choice(self, scene):
        if not [z for z in Engine.game.heroes if not z.unconscious]:
            return
        if (self.morale - 2 * Engine.game.heroes[0].level + random.randint(0, 50)) < 80:
            scene.exp -= self.exp
            scene.gold -= self.gold  # no exp, gold for enemies that run away
            scene.enemies.remove(self)
        elif self.magic:
            if random.randint(0, 128) < self.magic_chance:
                self.cast()
        elif self.skills:
            if random.randint(0, 128) < self.skill_chance:
                self.use()
        else:
            target = random.choice([0, 0, 0, 0, 1, 1, 2, 3])
            while Engine.game.heroes[target].incapacitated:
                target = random.choice([0, 0, 0, 0, 1, 1, 2, 3])
            return self.fight, Engine.game.heroes[target]

    def fight(self, target):
        if self.incapacitated:
            return
        damage = 0
        hit_chance = 168 + self.accuracy - target.evasion
        for i in range(int(1 + self.accuracy / 32)):
            if random.randint(0, 201) <= hit_chance:
                hit_damage = random.randint(self.attack, 2 * self.attack + 1) - target.defense
                damage += max(hit_damage, 1)
        target.hp -= damage

    def cast(self):
        pass
    def use(self):
        pass

    def draw(self):
        self.sprite.draw()

class Imp(Enemy):
    size = (32, 32)
    def __init__(self):
        super().__init__()
        self.maxhp = self.hp = 8
        self.attack = 4
        self.accuracy = 2
        self.hits = 1
        self.defense = 4
        self.evasion = 6
        self.mdefense = 16
        self.morale = 106
        self.species.add('Giant')
        self.gold = 6
        self.exp = 6
        self.sprite = pyglet.sprite.Sprite(Enemy.images.get_region(0, 0, 32, 32))

class MadPony(Enemy):
    size = (48, 48)
    def __init__(self):
        super().__init__()
        self.maxhp = self.hp = 64
        self.attack = 10
        self.accuracy = 16
        self.hits = 2
        self.defense = 2
        self.evasion = 22
        self.mdefense = 40
        self.morale = 106
        self.gold = 15
        self.exp = 63
        self.sprite = pyglet.sprite.Sprite(Enemy.images.get_region(240, 432, 48, 48))

class Formation:
    size = {(32, 32): 'S', (48, 48): 'M', (64, 64): 'L', (112, 96): 'XL'}
    def __init__(self, *args):
        self.enemies = args


class SceneBattle:

    class Cursor:
        sprite = pyglet.sprite.Sprite(pyglet.resource.image('cursor.png'))
        def __init__(self, matrix, pos=(0, 0)):
            self.matrix = matrix
            self.width = max([key[0] for key in self.matrix.keys()]) + 1
            self.height = max([key[1] for key in self.matrix.keys()]) + 1
            self.pos = self.menu_x, self.menu_y = pos
            self.x, self.y = self.matrix[(self.menu_x, self.menu_y)]

        def draw(self):
            self.sprite.x, self.sprite.y = self.x, self.y
            self.sprite.draw()

        def move_right(self):
            self.menu_x = (self.menu_x + 1) % self.width
            try:
                self.x, self.y = self.matrix[(self.menu_x, self.menu_y)]
            except KeyError:
                self.move_right()
        def move_left(self):
            self.menu_x = (self.menu_x - 1) % self.width
            try:
                self.x, self.y = self.matrix[(self.menu_x, self.menu_y)]
            except KeyError:
                self.move_left()
        def move_up(self):
            self.menu_y = (self.menu_y - 1) % self.height
            try:
                self.x, self.y = self.matrix[(self.menu_x, self.menu_y)]
            except KeyError:
                self.move_up()
        def move_down(self):
            self.menu_y = (self.menu_y + 1) % self.height
            try:
                self.x, self.y = self.matrix[(self.menu_x, self.menu_y)]
            except KeyError:
                self.move_down()

    def __init__(self, formation):
        self.formation = formation
        self.enemies = []
        sizes = [Formation.size[z.size] for z in self.formation.enemies]
        if 'XL' in sizes or 'L' in sizes:
            self.enemies = [self.formation.enemies[0]()]
        elif 'M' in sizes:
            if 'S' in sizes:
                pass
            for enemy in [z for z in self.formation.enemies if Formation.size[z.size] == 'M']:
                self.enemies.append(enemy())
            else:
                x, y = 16, 152
                for enemy in self.enemies:
                    enemy.sprite.x, enemy.sprite.y = x, y
                    y -= 48
                    if y == 56:
                        x += 48
                        y = 152
        else:
            x, y = 16, 168
            for enemy in self.formation.enemies:
                self.enemies.append(enemy())
                self.enemies[-1].sprite.x, self.enemies[-1].sprite.y = x, y
                y -= 32
                if y == 72:
                    x += 32
                    y = 168
        self.exp = sum([z.exp for z in self.enemies])
        self.gold = sum([z.gold for z in self.enemies])
        self.party_actions = []
        self.party_targets = []

        self.fixed = pyglet.graphics.Batch()
        self.menu = pyglet.graphics.Batch()
        self.layer_1 = pyglet.graphics.OrderedGroup(0)
        self.layer_2 = pyglet.graphics.OrderedGroup(1)
        self.layer_3 = pyglet.graphics.OrderedGroup(2)
        self.layer_4 = pyglet.graphics.OrderedGroup(3)
        self.text = pyglet.graphics.OrderedGroup(4)

        Engine.game.heroes[0].sprite.x, Engine.game.heroes[0].sprite.y = 176, 168
        Engine.game.heroes[1].sprite.x, Engine.game.heroes[1].sprite.y = 176, 144
        Engine.game.heroes[2].sprite.x, Engine.game.heroes[2].sprite.y = 176, 120
        Engine.game.heroes[3].sprite.x, Engine.game.heroes[3].sprite.y = 176, 96

        self.objects = [TextBox(128, 144,   8,  88, BLACK, self.fixed, self.layer_1),  # Enemy window
                        TextBox( 64, 144, 136,  88, BLACK, self.fixed, self.layer_1),  # Party window
                        TextBox( 48,  56, 200,  16, BLACK, self.fixed, self.layer_1),  # Hero 4 info
                        TextBox( 88,  80,   8,  16, BLACK, self.fixed, self.layer_2),  # Enemy names
                        TextBox( 48,  56, 200,  64, BLACK, self.fixed, self.layer_2),  # Hero 3 info
                        TextBox( 48,  56, 200, 112, BLACK, self.fixed, self.layer_3),  # Hero 2 info
                        TextBox( 48,  56, 200, 160, BLACK, self.fixed, self.layer_4),  # Hero 1 info
                        pyglet.text.Label('HP', x=208,  y=32, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HP', x=208,  y=80, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HP', x=208, y=128, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HP', x=208, y=176, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(Engine.game.heroes[3].name,
                                          x=208,  y=48, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(Engine.game.heroes[2].name,
                                          x=208,  y=96, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(Engine.game.heroes[1].name,
                                          x=208, y=144, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(Engine.game.heroes[0].name,
                                          x=208, y=192, font_size=8, batch=self.fixed, group=self.text),
                        TextBox(104,  80,  96,  16, BLACK, self.menu, self.layer_2),
                        pyglet.text.Label('FIGHT', x=112, y=72, font_size=8, batch=self.menu, group=self.text),
                        pyglet.text.Label('MAGIC', x=112, y=56, font_size=8, batch=self.menu, group=self.text),
                        pyglet.text.Label('DRINK', x=112, y=40, font_size=8, batch=self.menu, group=self.text),
                        pyglet.text.Label('ITEM',  x=112, y=24, font_size=8, batch=self.menu, group=self.text),
                        pyglet.text.Label('RUN',   x=160, y=72, font_size=8, batch=self.menu, group=self.text)]

        Engine.window.push_handlers(on_draw=self.on_draw)
        pyglet.clock.schedule_once(lambda dt: self.action_setup(), 3)

    def on_draw(self):
        Engine.window.clear()
        self.fixed.draw()
        for hero in Engine.game.heroes:
            hero.sprite.draw()
        for enemy in self.enemies:
            enemy.draw()
        hp_list = [pyglet.text.Label(str(Engine.game.heroes[0].hp), x=224, y=168, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[1].hp), x=224, y=120, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[2].hp), x=224, y=72, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[3].hp), x=224, y=24, font_size=8)]
        for hp_label in hp_list:
            hp_label.draw()
        return pyglet.event.EVENT_HANDLED  # so the default (blank) drawing doesn't take over

    def roll_back(self):
        Engine.game.heroes[len(self.party_actions)].sprite.x = 176
        if len(self.party_actions) > 0:
            self.party_actions.pop()
        if len(self.party_targets) > 0:
            self.party_targets.pop()

    def action_setup(self):
        if Engine.game.heroes[len(self.party_actions)].unconscious:
            self.party_actions.append(None)
            self.party_targets.append(None)
            if len(self.party_actions) == len(self.party_targets) == 4:
                self.round_setup()
            else:
                self.action_setup()
        Engine.game.heroes[len(self.party_actions)].sprite.x = 160
        Engine.window.set_handlers(on_draw=self.action_draw,
                                   on_key_press=self.action_key_press)
        self.cursor = SceneBattle.Cursor({(0, 0): (96, 64), (1, 0): (144, 64),
                                          (0, 1): (96, 48), (1, 1): (144, 64),
                                          (0, 2): (96, 32), (1, 2): (144, 64),
                                          (0, 3): (96, 16), (1, 3): (144, 64)})

    def action_draw(self):
        Engine.window.clear()
        self.fixed.draw()
        hp_list = [pyglet.text.Label(str(Engine.game.heroes[0].hp), x=224, y=168, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[1].hp), x=224, y=120, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[2].hp), x=224, y=72, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[3].hp), x=224, y=24, font_size=8)]
        for hp_label in hp_list:
            hp_label.draw()
        self.menu.draw()
        self.cursor.draw()
        for hero in Engine.game.heroes:
            hero.sprite.draw()
        for enemy in self.enemies:
            enemy.draw()
        return pyglet.event.EVENT_HANDLED

    def action_key_press(self, symbol, modifiers):
        if symbol in LEFT:
            self.cursor.move_left()
        elif symbol in RIGHT:
            self.cursor.move_right()
        if symbol in UP:
            self.cursor.move_up()
        elif symbol in DOWN:
            self.cursor.move_down()
        if symbol in BUTTON_A:
            if self.cursor.menu_x == 0 and self.cursor.menu_y == 0:
                index = len(self.party_actions)
                self.party_actions.append(Engine.game.heroes[index].fight)
                self.target_setup()
        if symbol in BUTTON_B:
            self.roll_back()
            self.action_setup()

        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

    def target_setup(self):
        Engine.window.set_handlers(on_draw=self.target_draw,
                                   on_key_press=self.target_key_press)
        cursor_keys = [(0, i) for i in range(len(self.enemies))]
        cursor_values = [(enemy.sprite.x-16, enemy.sprite.y+16) for enemy in self.enemies]
        cursor_matrix = dict(list(zip(cursor_keys, cursor_values)))
        self.cursor = SceneBattle.Cursor(cursor_matrix)

    def target_draw(self):
        Engine.window.clear()
        self.fixed.draw()
        self.menu.draw()
        self.cursor.draw()
        for hero in Engine.game.heroes:
            hero.sprite.draw()
        for enemy in self.enemies:
            enemy.draw()
        hp_list = [pyglet.text.Label(str(Engine.game.heroes[0].hp), x=224, y=168, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[1].hp), x=224, y=120, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[2].hp), x=224, y=72, font_size=8),
                   pyglet.text.Label(str(Engine.game.heroes[3].hp), x=224, y=24, font_size=8)]
        for hp_label in hp_list:
            hp_label.draw()
        return pyglet.event.EVENT_HANDLED

    def target_key_press(self, symbol, modifiers):
        if symbol in LEFT:
            self.cursor.move_left()
        elif symbol in RIGHT:
            self.cursor.move_right()
        if symbol in UP:
            self.cursor.move_up()
        elif symbol in DOWN:
            self.cursor.move_down()
        if symbol in BUTTON_A:
            Engine.game.heroes[len(self.party_targets)].sprite.x = 176
            target = self.cursor.menu_x * self.cursor.height + self.cursor.menu_y
            self.party_targets.append(self.enemies[target])
            if len(self.party_actions) == len(self.party_targets) == 4:
                self.round_setup()
            else:
                self.action_setup()
        if symbol in BUTTON_B:
            try:
                self.party_actions.pop()
            except IndexError:
                pass
            self.action_setup()

        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

    def round_setup(self):
        party_moves = list(zip(self.party_actions, self.party_targets))
        enemy_moves = [enemy.ai_choice(self) for enemy in self.enemies]
        moves = party_moves + enemy_moves
        random.shuffle(moves)
        for move in moves:
            if not move == (None, None):
                if not move[1].incapacitated:
                    move[0](move[1])
                    if self.check_win():
                        return
        self.party_actions = []
        self.party_targets = []
        self.enemies = [z for z in self.enemies if not z.incapacitated]
        self.action_setup()

    def check_win(self):
        us = [hero for hero in Engine.game.heroes if not hero.incapacitated]
        them = [enemy for enemy in self.enemies if not enemy.incapacitated]
        if not them:
            print('You won!')
            for hero in us:
                next_level = [z for z in hero.exp_levels if z > hero.exp][0]
                hero.exp += self.exp // len(us)
                if hero.exp >= next_level:
                    stat_ups = hero.level_up()
                    print('{} + {}'.format(hero.name, stat_ups))
            Engine.game.gold += self.gold

            Engine.window.pop_handlers()
            return True
        elif not us:
            print('You lost!')
            Engine.window.pop_handlers()
            return True
        return False

if __name__ == "__main__":
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    scene = SceneBattle(Formation(Imp, Imp))
    pyglet.app.run()
