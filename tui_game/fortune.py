import random

def dices():
    """Simulating dices with random function"""

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return [dice_1, dice_2]


def decides_who_start():
    """method to decide who starts game, using  random"""

    while True:
        dice_1 = random.randint(1, 6)  # white
        dice_2 = random.randint(1, 6)  # black
        if dice_1 < dice_2:
            return True  # black start
        if dice_1 > dice_2:
            return False  # white start