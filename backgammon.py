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


if __name__ == "__main__":
    main()
