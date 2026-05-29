class Wojownik:
    def __init__(self, name):
        self.name = name
        self.life = 150
        self.mana = 80
        self.strength = 15
        self.maxmana = 80
        self.maxlife = 150
        self.maxstrength = 15
        self.level = 1
        self.experience = 0
        self.next_level_exp = 100
        self.speed = 15
        self.defense = 8
        self.dodge_chance = 0.03
        self.critical_chance = 0.03
        self.critical_multiplier = 2

class Mag:
    def __init__(self, name):
        self.name = name
        self.life = 90
        self.mana = 150
        self.strength = 7
        self.maxmana = 150
        self.maxlife = 90
        self.maxstrength = 7
        self.level = 1
        self.experience = 0
        self.next_level_exp = 100
        self.speed = 20
        self.defense = 3
        self.dodge_chance = 0.01
        self.critical_chance = 0.05
        self.critical_multiplier = 3

class Tank:
    def __init__(self, name):
        self.name = name
        self.life = 300
        self.mana = 80
        self.strength = 5
        self.maxmana = 80
        self.maxlife = 300
        self.maxstrength = 5
        self.level = 1
        self.experience = 0
        self.next_level_exp = 100
        self.speed = 5
        self.defense = 15
        self.dodge_chance = 0.01
        self.critical_chance = 0.01
        self.critical_multiplier = 2

class Lucznik:
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.mana = 100
        self.strength = 10
        self.maxmana = 100
        self.maxlife = 100
        self.maxstrength = 10
        self.level = 1
        self.experience = 0
        self.next_level_exp = 100
        self.speed = 25
        self.defense = 5
        self.dodge_chance = 0.02
        self.critical_chance = 0.04
        self.critical_multiplier = 2.5
