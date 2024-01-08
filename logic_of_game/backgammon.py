class Backgammon:
    def __init__(self):
        """
        initialization of game with default variables
           tabla = represent the real game board with 24 columns
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

    def reset(self):
        """
        method to reset the game
        :return: nothing
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

    def __str__(self):
        """
        method to print the class
        :return: string representation of the class
        """
        up = self.tabla[:12]
        up.reverse()
        down = self.tabla[12:]
        return str(up) + "\n\n\n" + str(down) + "\n" + "Retrase albe = " + str(
            self.white_set) + "\n" + "Retrase negre = " + str(self.black_set) + "\n" + "Scoase albe = " + str(
            self.remove_white) + "\n" + "Scoase negre = " + str(self.remove_black)

    def can_remove_piece(self, player):
        """
        checks if the player can remove the piece on the board
        :param player:
        :return: False when the player cannot remove the piece, True otherwise
        """
        if player == self.white:
            for i in range(6, 24):
                if self.tabla[i] > 0:
                    return False
            if self.remove_white != 0:
                return False
            return True
        if player == self.black:
            for i in range(0, 18):
                if self.tabla[i] < 0:
                    return False
            if self.remove_black != 0:
                return False
            return True

    def win_what(self):
        """
        method for:
            1. checking the game status (if it's finished or not)
            2. determining the winner
        :return: 1 if white win, -1 if black win, False otherwise
        """
        if self.white_set == 15:
            return 1
        if self.black_set == 15:
            return -1
        else:
            return False
