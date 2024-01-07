from tui_game import backgammon


def move_piece(situation: backgammon.Backgammon, player, list_of_possible_moves: dict, begin, finish):
    if begin < 0 or finish < -1:
        print("Illegal move: nu esti zdravan la cap")
        return False
    elif begin not in list_of_possible_moves.keys():
        print("Illegal move, nu ai cum")
        return False
    elif finish not in list_of_possible_moves[begin]:
        print("Illegal move: nu poti muta acolo")
        return False
    elif not situation.can_remove_piece(player) and finish == -1:
        print("Illegal move: nu ai toate piesele in casa ta")
        return False
    else:
        if player == situation.white:
            if finish == -1:
                situation.tabla[begin] -= 1
                situation.white_set += 1
                return begin + 1
            elif situation.tabla[finish] == -1:
                situation.remove_black += 1
                situation.tabla[begin] -= 1
                situation.tabla[finish] += 2
                return begin - finish
            else:
                situation.tabla[begin] -= 1
                situation.tabla[finish] += 1
                return begin - finish
        if player == situation.black:
            if finish == -1:
                situation.tabla[begin] += 1
                situation.black_set += 1
                return 24 - begin
            elif situation.tabla[finish] == 1:
                situation.remove_white += 1
                situation.tabla[begin] += 1
                situation.tabla[finish] -= 2
                return finish - begin
            else:
                situation.tabla[begin] += 1
                situation.tabla[finish] -= 1
                return finish - begin


def move_piece_on_table(situation: backgammon.Backgammon, player, list_of_possible_move, finish):
    if finish < 0:
        print("Illegal move: nu esti zdravan la cap")
        return False
    elif finish not in list_of_possible_move:
        print("Illegal move, nu poti pune acolo")
        return False
    else:
        if player == situation.white:
            if situation.tabla[finish] == -1:
                situation.tabla[finish] += 1
                situation.remove_black += 1
            situation.tabla[finish] += 1
            situation.remove_white -= 1
            return (24 - finish - 1) % 6 + 1
        if player == situation.black:
            if situation.tabla[finish] == 1:
                situation.tabla[finish] -= 1
                situation.remove_white += 1
            situation.tabla[finish] -= 1
            situation.remove_black -= 1
            return finish % 6 + 1
