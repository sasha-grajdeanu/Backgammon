import fortune
import backgammon
import move_player_white
import move_player_black
import moves_ai_player_black
import move_ai_player_white


def game_h_vs_h():
    game = backgammon.Backgammon()
    turn = 0
    start_player = fortune.decides_who_start()
    if start_player:
        turn = -1
    else:
        turn = 1
    while True:
        # print(game)
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

def game_h_vs_ai():
    game = backgammon.Backgammon()
    establish_ai = fortune.decides_who_start()
    if establish_ai:
        print("AI = BLACK")
    else:
        print("AI = WHITE")
    turn = 0
    start_player = fortune.decides_who_start()
    if start_player:
        turn = -1
    else:
        turn = 1
    while True:
        # print(game)
        if game.win_what() == 1:
            print("White win")
            break
        if game.win_what() == -1:
            print("Black win")
            break
        else:
            if turn == -1:
                print("BLACK TURN")
                if establish_ai:
                    moves_ai_player_black.move_ai_black(game)
                else:
                    move_player_black.move_black(game)
                turn = 1
            else:
                print("WHITE TURN")
                if not establish_ai:
                    move_ai_player_white.move_ai_white(game)
                else:
                    move_player_white.move_white(game)
                turn = -1
