import random


class LightWarrior:
    class_name = "NONE"

    def __init__(self):
        self.name = ''
        self.level = 1
        self._hp = 1
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.vitality = 1
        self.luck = 1
        self.accuracy = 1
        self.mdefense = 1
        self.status = set()
        self.weapons = []
        self.armor = []
        self.exp = 0

    # TODO: make statuses instances of Status that report whether they incapacitate/disable/etc.
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
    def defense(self):
        return sum([z.absorb for z in self.armor], 0)

    @property
    def evasion(self):
        return 48 + self.agility - sum([z.weight for z in self.armor], 0)

    @property
    def attack(self):
        return sum([z.attack for z in self.weapons], self.strength // 2)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        self._hp = max(0, self._hp)
        if self._hp == 0:
            self.status.add('Dead')

    def fight(self, target):
        if self.incapacitated:
            return
        damage = 0
        hit_chance = sum([z.accuracy for z in self.weapons], 168 + self.accuracy - target.evasion)
        hits = 1 + sum([z.accuracy for z in self.weapons], self.accuracy) // 32
        for i in range(hits):
            if random.randint(0, 201) <= hit_chance:
                hit_damage = random.randint(self.attack, 2 * self.attack + 1) - target.defense
                damage += max(hit_damage, 1)
        target.hp -= damage
