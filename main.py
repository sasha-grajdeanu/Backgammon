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
    game.tabla[0] = 2
    game.tabla[1] = -2
    game.tabla[2] = 0
    game.tabla[3] = -1
    game.tabla[4] = 0
    game.tabla[5] = 2

    game.remove_black = 2

    print(game)

    move_player_black.move_black(game)

    print(game)


if __name__ == "__main__":
    main()