from copy import deepcopy
from logic_of_game import backgammon


def available_move(situation: backgammon.Backgammon, player, dice_1, dice_2, double=None):
    """
    Method for calculating the available move of a player with dice_1 and dice_2
    :param situation: current status of backgammon table
    :param player: player who wants to move
    :param dice_1: dice 1
    :param dice_2: dice 2
    :param double: if dice_1 == dice_2 then need to use other method for calculating the moves
    :return: dictionary with available moves
    """
    list_of_possible_moves = dict()
    if player == situation.black:
        if situation.can_remove_piece(situation.black):
            for i in range(18, 24):
                if situation.tabla[i] < 0:
                    break
                else:
                    if dice_1 == 24 - i:
                        dice_1 -= 1
                    if dice_2 == 24 - i:
                        dice_2 -= 1
        for i in range(len(situation.tabla)):
            if situation.tabla[i] < 0:
                list_of_movement = set()
                if double is None:
                    list_of_movement.add(i + dice_1)
                    list_of_movement.add(i + dice_2)
                    if i in list_of_movement:
                        list_of_movement.remove(i)
                else:
                    if double is None:
                        return list_of_possible_moves
                    for j in range(double):
                        list_of_movement.add(i + dice_1)
                    if i in list_of_movement:
                        list_of_movement.remove(i)
                flag = False
                list_of_movement = list(list_of_movement)
                for element in deepcopy(list_of_movement):
                    if situation.can_remove_piece(situation.black):
                        if element > 24:
                            list_of_movement.remove(element)
                        elif element == 24:
                            list_of_movement.remove(element)
                            flag = True
                        elif situation.tabla[element] > 1:
                            list_of_movement.remove(element)
                    else:
                        if element > 23:
                            list_of_movement.remove(element)
                        elif situation.tabla[element] > 1:
                            list_of_movement.remove(element)
                if flag:
                    list_of_movement.append(-1)
                if len(list_of_movement) != 0:
                    list_of_possible_moves[i] = list_of_movement
    if player == situation.white:
        if situation.can_remove_piece(situation.white):
            for i in range(0, 6).__reversed__():
                if situation.tabla[i] > 0:
                    break
                else:
                    if dice_1 == i + 1:
                        dice_1 -= 1
                    if dice_2 == i + 1:
                        dice_2 -= 1

        for i in range(len(situation.tabla)).__reversed__():
            if situation.tabla[i] > 0:
                list_of_movement = set()
                if double is None:
                    list_of_movement.add(i - dice_1)
                    list_of_movement.add(i - dice_2)
                    if i in list_of_movement:
                        list_of_movement.remove(i)
                else:
                    for j in range(double):
                        list_of_movement.add(i - dice_1)
                    if i in list_of_movement:
                        list_of_movement.remove(i)

                flag = False
                list_of_movement = list(list_of_movement)
                for element in deepcopy(list_of_movement):
                    if situation.can_remove_piece(situation.white):
                        if element < -1:
                            list_of_movement.remove(element)
                        elif element == -1:
                            list_of_movement.remove(element)
                            flag = True
                        elif situation.tabla[element] < -1:
                            list_of_movement.remove(element)
                    else:
                        if element < 0:
                            list_of_movement.remove(element)
                        elif situation.tabla[element] < -1:
                            list_of_movement.remove(element)
                if flag:
                    list_of_movement.append(-1)
                if len(list_of_movement) != 0:
                    list_of_possible_moves[i] = list_of_movement
    return list_of_possible_moves


def where_can_place_piece(situation: backgammon.Backgammon, player, dice_1, dice_2):
    """
    Used when the player have pieces removed by the opponent
    Method for calculating the available movements
    :param situation: situation: current status of backgammon table
    :param player: player who wants to move
    :param dice_1: dice 1
    :param dice_2: dice 2
    :return: a list with the available movements
    """
    list_of_possible_place = set()
    if player == situation.white:
        list_of_possible_place.add(24 - dice_1)
        list_of_possible_place.add(24 - dice_2)
        for elem in deepcopy(list_of_possible_place):
            if elem == 24:
                list_of_possible_place.remove(elem)
            elif situation.tabla[elem] < -1:
                list_of_possible_place.remove(elem)
    if player == situation.black:
        list_of_possible_place.add(-1 + dice_1)
        list_of_possible_place.add(-1 + dice_2)
        for elem in deepcopy(list_of_possible_place):
            if elem == -1:
                list_of_possible_place.remove(elem)
            elif situation.tabla[elem] > 1:
                list_of_possible_place.remove(elem)
    return list(list_of_possible_place)
