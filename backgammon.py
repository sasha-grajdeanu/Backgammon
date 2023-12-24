import random
from copy import deepcopy


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

    def can_remove_piece(self, player):

        """method to check if a player can remove pieces """

        if player == self.white:
            if sum(self.tabla[:6]) == 15:
                return True
            return False
        if player == self.black:
            if sum(self.tabla[18:]) == -15:
                return True
            return False

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
                    flag = False
                    for element in deepcopy(list_of_movement):
                        print(element)
                        if element > 23:
                            print(element)
                            flag = True
                            list_of_movement.remove(element)
                            # aici putem zice ca ar putea fi scoasa din tabla
                        elif self.tabla[element] > 1:  # romanian : este poarta in casa facuta de adversar
                            list_of_movement.remove(element)
                    if flag:
                        list_of_movement.append(-1)
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
                    flag = False

                    for element in deepcopy(list_of_movement):
                        if element < 0:
                            print(element)
                            print("hey")
                            flag = True
                            list_of_movement.remove(element)
                            # aici putem zice ca ar putea fi scoasa din tabla
                        elif self.tabla[element] < -1:  # romanian : este poarta in casa facuta de adversar
                            list_of_movement.remove(element)
                    if flag:
                        list_of_movement.append(-1)
                    list_of_possible_movement[i] = list_of_movement
        return list_of_possible_movement

    def move_piece(self, player: int, list_of_possible_movement: dict, begin: int, finish: int):

        """method for move a piece in table"""

        if begin < 0 or finish < -1:
            print("Illegal move: nu esti zdravan la cap")
            return False
        elif begin not in list_of_possible_movement.keys():
            print("Illegal move, nu ai piese acolo")
            return False
        elif finish not in list_of_possible_movement[begin]:
            print("Illegal move: nu poti muta acolo")
            return False
        elif not self.can_remove_piece(player) and finish == -1:
            print("Illegal move: nu ai toate piesele in casa ta")
            return False
        else:
            if player == self.white:
                if finish == -1:
                    self.tabla[begin] -= 1
                    self.white_set += 1
                    return True
                else:
                    self.tabla[begin] -= 1
                    self.tabla[finish] += 1
                    return begin - finish
            if player == self.black:
                if finish == -1:
                    self.tabla[begin] += 1
                    self.black_set += 1
                    return True
                else:
                    self.tabla[begin] += 1
                    self.tabla[finish] -= 1
                    return finish - begin
            print(self)

    def move_player(self, player):
        dice_1, dice_2 = self.dices()
        if dice_1 == dice_2:
            sum = 4 * dice_1
        else:
            sum = dice_1 + dice_2
        if player == self.white:
            pos_moves = self.availble_moves(player, dice_1, dice_2)
            print(pos_moves)
            while sum != 0:
                # aici trebuie sa luam mai multe cazuri (like e scoasa o piesa etc)
                """
                    Deci, trebuie tratat urmatoarele cazuri:
                        1. daca o piesa este scoasa intr-o runda anterioara si trebuie pusa
                        2. cand scoate afara o piesa de a lui
                        3. cand scoate afara o piesa de a adversarului
                        4. cand muta normal
                        5. daca nu sunt mutari posibile
                """
                position = int(input("what piece would you like to move"))
                finish = int(input("where would you like to move"))
                result = self.move_piece(player, position, finish)
                if result != False:
                    pass

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
