class Bossy:
    def __init__(self, name, life, strength, speed, defense, gold, experience):
        self.name = name
        self.life = life
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.gold = gold
        self.experience = experience
class Rakanoth(Bossy):
    def __init__(self):
        super().__init__("Rakanoth", 500, 30, 20, 10, 150, 100)
class Adria(Bossy):
    def __init__(self):
        super().__init__("Adria", 400, 25, 25, 15 , 200, 150)
class Diablo(Bossy):
    def __init__(self):
        super().__init__("Diablo", 600, 35, 15, 20, 250, 200)