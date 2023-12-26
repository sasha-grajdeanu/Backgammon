import math

import math_moves
import fortune
import backgammon
import move_piece
import move_player_white
import move_player_black


def main():
    game = backgammon.Backgammon()
    # print(game)
    # print(fortune.dices())

    print(game)
    game.tabla[0] = 0
    game.tabla[11] = 0
    game.tabla[16] = 0

    game.tabla[18] = 0
    game.tabla[19] = 0
    game.tabla[20] = -3
    game.tabla[21] = -5
    game.tabla[22] = -2
    game.tabla[23] = -5

    move_player_black.move_black(game)

    print(game)


if __name__ == "__main__":
    main()