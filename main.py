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

    # print(game)
    game.tabla[23] = 0
    game.tabla[12] = 0
    game.tabla[7] = 0

    game.tabla[5] = 1
    game.tabla[4] = 1
    game.tabla[3] = 2
    game.tabla[2] = 1
    game.tabla[1] = 5
    game.tabla[0] = 5

    print(game)

    print(math_moves.available_move(game, game.white, 5, 5, 4))
    # move_player_black.move_black(game)
    # for i in range(0, 6).__reversed__():
    #     print(i)

    print(game)


if __name__ == "__main__":
    main()