import fortune
import backgammon
import move_player_white
import move_player_black


def game():
    game = backgammon.Backgammon()
    turn = 0
    start_player = fortune.decides_who_start()
    if start_player:
        turn = -1
    else:
        turn = 1
    while True:
        print(game)
        if game.win_what() == 1:
            print("White win")
            break
        if game.win_what() == -1:
            print("Black win")
            break
        else:
            if turn == -1:
                print("BLACK TURN")
                move_player_black.move_black(game)
                turn = 1
            else:
                print("WHITE TURN")
                move_player_white.move_white(game)
                turn = -1
