from copy import deepcopy

import backgammon


def available_move(situation: backgammon.Backgammon, player, dice_1, dice_2, double=None):
    list_of_possible_moves = dict()
    if player == situation.black:
        if situation.can_remove_piece(situation.black):
            for i in range(0, 6):
                # print("hey")
                if 24 - i == dice_1 and situation.tabla[i] >= 0:
                    dice_1 -= 1
                if 24 - i == dice_2 and situation.tabla[i] >= 0:
                    dice_2 -= 1
                else:
                    break
        for i in range(len(situation.tabla)):
            print(dice_1, dice_2)
            if situation.tabla[i] < 0:
                list_of_movement = set()
                if dice_1 != dice_2:
                    list_of_movement.add(i + dice_1)
                    list_of_movement.add(i + dice_2)
                    list_of_movement.add(i + dice_1 + dice_2)
                    if i in list_of_movement:
                        list_of_movement.remove(i)
                else:
                    if double is None:
                        return list_of_possible_moves
                    for j in range(double):
                        list_of_movement.add(i + (j + 1) * dice_1)
                flag = False
                list_of_movement = list(list_of_movement)
                for element in deepcopy(list_of_movement):
                    if situation.can_remove_piece(situation.black):
                        if element > 24:
                            list_of_movement.remove(element)
                            # flag = True
                        elif element == 24:
                            list_of_movement.remove(element)
                            flag = True
                        elif situation.tabla[element] > 1:
                            list_of_movement.remove(element)
                    else:
                        if element > 23:
                            flag = True
                            list_of_movement.remove(element)
                        elif situation.tabla[element] > 1:
                            list_of_movement.remove(element)
                if flag:
                    list_of_movement.append(-1)
                list_of_possible_moves[i] = list_of_movement
    if player == situation.white:
        if situation.can_remove_piece(situation.white):
            for i in range(0, 6):
                print("hey")
                if i + 1 == dice_1 and situation.tabla[i] <= 0:
                    dice_1 -= 1
                if i + 1 == dice_2 and situation.tabla[i] <= 0:
                    dice_2 -= 1
                else:
                    break
        for i in range(len(situation.tabla)).__reversed__():
            print(dice_1, dice_2)
            if situation.tabla[i] > 0:
                list_of_movement = set()
                if dice_1 != dice_2:
                    list_of_movement.add(i - dice_1)
                    list_of_movement.add(i - dice_2)
                    list_of_movement.add(i - dice_1 - dice_2)
                    if i in list_of_movement:
                        list_of_movement.remove(i)
                else:
                    if double is None:
                        return list_of_possible_moves
                    for j in range(double):
                        list_of_movement.add(i - (j + 1) * dice_1)

                flag = False
                list_of_movement = list(list_of_movement)
                for element in deepcopy(list_of_movement):
                    if situation.can_remove_piece(situation.white):
                        if element < -1:
                            list_of_movement.remove(element)
                            # flag = True
                        elif element == -1:
                            list_of_movement.remove(element)
                            flag = True
                        elif situation.tabla[element] < -1:
                            list_of_movement.remove(element)
                    else:
                        if element > 0:
                            flag = True
                            list_of_movement.remove(element)
                        elif situation.tabla[element] > -1:
                            list_of_movement.remove(element)
                if flag:
                    list_of_movement.append(-1)
                list_of_possible_moves[i] = list_of_movement
    return list_of_possible_moves


def where_can_place_piece(situation: backgammon.Backgammon, player, dice_1, dice_2):
    list_of_possible_place = list()
    if player == situation.white:
        list_of_possible_place.append(24 - dice_1)
        list_of_possible_place.append(24 - dice_2)
        for elem in deepcopy(list_of_possible_place):
            if elem == 24:
                list_of_possible_place.remove(elem)
            elif situation.tabla[elem] < -1:
                list_of_possible_place.remove(elem)
    if player == situation.black:
        list_of_possible_place.append(-1 + dice_1)
        list_of_possible_place.append(-1 + dice_2)
        for elem in deepcopy(list_of_possible_place):
            if elem == 0:
                list_of_possible_place.remove(elem)
            elif situation.tabla[elem] > 1:
                list_of_possible_place.remove(elem)
    return list_of_possible_place
