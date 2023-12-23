import random


class Backgammon:
    def __init__(self):
        self.tabla = list(0 for i in range(24))
        self.tabla[23] = 2
        self.tabla[18] = -5
        self.tabla[16] = -3
        self.tabla[12] = 5
        self.tabla[11] = -5
        self.tabla[7] = 3
        self.tabla[5] = 5
        self.tabla[0] = -2
        self.remove_white = 0
        self.remove_black = 0
        self.white_set = 0
        self.black_set = 0
        self.white = 1
        self.black = -1

    def reset(self):
        self.tabla = list(0 for i in range(24))
        self.tabla[23] = 2
        self.tabla[18] = -5
        self.tabla[16] = -3
        self.tabla[12] = 5
        self.tabla[11] = -5
        self.tabla[7] = 3
        self.tabla[5] = 5
        self.tabla[0] = -2
        self.remove_white = 0
        self.remove_black = 0
        self.white_set = 0
        self.black_set = 0

    def dices(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        return dice_1, dice_2

    def decides_who_start(self):
        while True:
            dice_1 = random.randint(1, 6)  # white
            dice_2 = random.randint(1, 6)  # black
            if dice_1 < dice_2:
                return True  # black start
            if dice_1 > dice_2:
                return False  # white start

    def __str__(self):
        up = self.tabla[:12]
        up.reverse()
        down = self.tabla[12:]
        return str(up) + "\n\n\n" + str(down) + "\n" + "Retrase albe = " + str(
            self.white_set) + "\n" + "Retrase negre = " + str(self.black_set) + "\n" + "Scoase albe = " + str(
            self.remove_white) + "\n" + "Scoase negre = " + str(self.remove_black)


def main():
    game = Backgammon()
    print(game)
    x, y = game.dices()
    print(x, y)
    print(game.decides_who_start())


if __name__ == "__main__":
    main()
