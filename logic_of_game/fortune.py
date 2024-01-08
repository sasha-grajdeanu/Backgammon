import random


def dices():
    """
    Simulating dices with random function
    :return: a list with random numbers which represent 2 dices
    """
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return [dice_1, dice_2]


def decides_who_start():
    """
    Determines what player will start the game + used for establish what player will be AI
    :return: True for black, False for white
    """
    while True:
        dice_1 = random.randint(1, 6)  # white
        dice_2 = random.randint(1, 6)  # black
        if dice_1 < dice_2:
            return True  # black start
        if dice_1 > dice_2:
            return False  # white start
