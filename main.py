import math

import math_moves
import fortune
import backgammon
import move_piece


def main():
    game = backgammon.Backgammon()
    print(game)
    print(fortune.dices())
    print(math_moves.available_move(game, game.white, 3, 4))
    print(move_piece.move_piece(game, game.white, math_moves.available_move(game, game.white, 3, 4), 5, 2))
    print(move_piece.move_piece(game, game.white, math_moves.available_move(game, game.white, 3, 4), 5, 1))
    print(game)
    print(game.can_remove_piece(game.white))
    print(fortune.decides_who_start())
if __name__ == "__main__":
    main()