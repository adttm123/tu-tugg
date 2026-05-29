import random

potwor = []

def goblin():
    
    potwor[:] = ["Goblin", random.randint(30, 50), random.randint(10, 20)]

def ultra_goblin():
    
    potwor[:] = ["Ultra goblin", random.randint(50, 70), random.randint(20, 30)]

def szczur_morski():

    potwor[:] = ["Szczur morski", random.randint(10, 30), random.randint(5, 10)]

def Scylla():
    potwor[:] = ["Scylla", random.randint(200, 300), random.randint(40, 60)]

def losuj_potwora():
    los = random.randint(1, 100)
    if los <= 50:
        szczur_morski()
    elif los <= 80:
        goblin()
    elif los <= 99:
        ultra_goblin()
    else:
        Scylla()
    return potwor

boss = []

def Siegebreaker_Assault_Beast():
    boss[:] = ["Siegebreaker_Assault_Beast", random.randint(1000, 8000), 200]

def Diablo():
    boss[:] = ["Diablo", random.randint(8000, 80000), 400]

def losuj_bossa():
    lo = random.randint(1, 100)
    if lo <= 99:
        Siegebreaker_Assault_Beast()
    else:
        Diablo()
    return boss