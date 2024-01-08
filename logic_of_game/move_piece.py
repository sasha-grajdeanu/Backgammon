from logic_of_game import backgammon


def move_piece(situation: backgammon.Backgammon, player, list_of_possible_moves: dict, begin, finish):
    """
    Method for moving a piece in backgammon table in usual case
    :param situation: current status of backgammon table
    :param player: player who wants to move the piece
    :param list_of_possible_moves: available moves of player
    :param begin: position from where he wants to move
    :param finish: position where he wants to move
    :return: False if move is invalid, dice used otherwise
    """
    if begin < 0 or finish < -1:
        print("Illegal move: O.M.G.")
        return False
    elif begin not in list_of_possible_moves.keys():
        print("Illegal move, u don't have piece there")
        return False
    elif finish not in list_of_possible_moves[begin]:
        print("Illegal move: u can't move there")
        return False
    elif not situation.can_remove_piece(player) and finish == -1:
        print("Illegal move: u don't have all piece on inner section")
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
    """
    Used then the player need to put the removed pieces on backgammon table
    :param situation: current status of backgammon table
    :param player: player who want to move the piece
    :param list_of_possible_move: available moves of player
    :param finish: position where the player want to put the piece
    :return: False if move is invalid, used dice otherwise
    """
    if finish < 0:
        print("Illegal move: O.M.G.")
        return False
    elif finish not in list_of_possible_move:
        print("Illegal move, u can't move there")
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
