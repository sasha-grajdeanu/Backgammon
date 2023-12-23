import random


class Backgammon:
    def __init__(self):

        """initialization of game with default variables
           tabla = represent the real gameboard with 24 columns
           remove_color (where color is black or white) represent the pieces removed by opponent
           color_set (where color is black or white) represent the pieces removed by the player with the same color
        """

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

    def dices(self):

        """Simulating dices with random function"""

        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        return dice_1, dice_2

    def decides_who_start(self):

        """method to decide who starts game, using  random"""

        while True:
            dice_1 = random.randint(1, 6)  # white
            dice_2 = random.randint(1, 6)  # black
            if dice_1 < dice_2:
                return True  # black start
            if dice_1 > dice_2:
                return False  # white start

    def availble_moves(self, player, dices_1, dices_2):

        """method for calculate possible movement of player"""

        list_of_possible_movement = dict()
        if player == self.black:
            for i in range(len(self.tabla)):
                if self.tabla[i] < 0:  # means there are black pieces on that position
                    list_of_movement = list()
                    if dices_1 != dices_2:
                        list_of_movement.append(i + dices_1)
                        list_of_movement.append(i + dices_2)
                        list_of_movement.append(i + dices_1 + dices_2)
                    else:  # dubla
                        list_of_movement.append(i + dices_1)
                        list_of_movement.append(i + 2 * dices_1)
                        list_of_movement.append(i + 3 * dices_1)
                        list_of_movement.append(i + 4 * dices_1)
                    for element in list_of_movement:
                        if element > 23:
                            continue  # aici putem zice ca ar putea fi scoasa din tabla
                        if self.tabla[element] > 1:  # romanian : este poarta in casa facuta de adversar
                            list_of_movement.remove(element)
                    list_of_possible_movement[i] = list_of_movement
        if player == self.white:
            for i in range(len(self.tabla)):
                if self.tabla[i] > 0:  # means there are white pieces on that position
                    list_of_movement = list()
                    if dices_1 != dices_2:
                        list_of_movement.append(i - dices_1)
                        list_of_movement.append(i - dices_2)
                        list_of_movement.append(i - dices_1 - dices_2)
                    else:  # dubla
                        list_of_movement.append(i - dices_1)
                        list_of_movement.append(i - 2 * dices_1)
                        list_of_movement.append(i - 3 * dices_1)
                        list_of_movement.append(i - 4 * dices_1)
                    for element in list_of_movement:
                        if element < 0:
                            continue  # aici putem zice ca ar putea fi scoasa din tabla
                        if self.tabla[element] < -1:  # romanian : este poarta in casa facuta de adversar
                            list_of_movement.remove(element)
                    list_of_possible_movement[i] = list_of_movement
        return list_of_possible_movement

    def move_piece(self, player, list_of_possible_movement: dict, begin, finish):
        if begin < 0 or finish < 0:
            print("Illegal move")
            return False
        elif begin not in list_of_possible_movement.keys():
            print("Illegal move")
            return False
        elif finish not in list_of_possible_movement[begin]:
            print("Illegal move")
            return False
        else:
            if player == self.white:
                self.tabla[begin] -= 1
                self.tabla[finish] += 1
            if player == self.black:
                self.tabla[begin] += 1
                self.tabla[finish] -= 1
            print(self)
            return True

    def __str__(self):

        """overwriting __str__ method, adapt for my class"""

        up = self.tabla[:12]
        up.reverse()
        down = self.tabla[12:]
        return str(up) + "\n\n\n" + str(down) + "\n" + "Retrase albe = " + str(
            self.white_set) + "\n" + "Retrase negre = " + str(self.black_set) + "\n" + "Scoase albe = " + str(
            self.remove_white) + "\n" + "Scoase negre = " + str(self.remove_black)


def main():
    """debugging and testing functionality"""

    game = Backgammon()
    print(game)
    x, y = game.dices()
    print(x, y)
    print(game.decides_who_start())
    s = game.availble_moves(1, 3, 3)
    print(s)
    print(list(s.keys()))
    print(game.move_piece(1, s, 5, 2))


if __name__ == "__main__":
    main()
