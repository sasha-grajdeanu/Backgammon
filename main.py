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

    move_player_white.move_white(game)

    print(game)


if __name__ == "__main__":
    main()