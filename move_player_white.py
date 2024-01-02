import backgammon as bk
import fortune as frt
import math_moves
import move_piece


def move_white(sit: bk.Backgammon):
    dice_1, dice_2 = frt.dices()
    print("zaruri date", dice_1, dice_2)
    if dice_1 != dice_2:
        sum = 2
    else:
        sum = 4

    while sum != 0:
        if isinstance(sit.win_what(), bool):
            print("sum", sum)
            print(sit)
            if dice_1 != dice_2:
                list_of_possible_move = math_moves.available_move(sit, sit.white, dice_1, dice_2)
            else:
                list_of_possible_move = math_moves.available_move(sit, sit.white, dice_1, dice_2, sum)
            if len(list_of_possible_move) == 0:
                # blocaj
                print("BLOCAJ 1")
                return -1
            if sit.remove_white != 0:
                # inseamna ca trebuie sa pun piesa pe tabla in casa adversarului
                list_of_possible_move_on_adversary = math_moves.where_can_place_piece(sit, sit.white, dice_1, dice_2)
                print("list", list_of_possible_move_on_adversary)
                if len(list_of_possible_move_on_adversary) == 0:
                    print("BLOCAJ 2")
                    return -1
                else:
                    while True:
                        try:
                            finish = int(input("linia unde pui piesa "))
                        except ValueError:
                            print("NOT INTEGER")
                            continue
                        else:
                            break
                    # print("decizie", finish)
                    result = move_piece.move_piece_on_table(sit, sit.white, list_of_possible_move_on_adversary, finish)
                    # print("res", result)
                    if isinstance(result, bool):
                        print("Nu merge")
                    else:
                        if dice_1 != dice_2:
                            # normal
                            sum -= 1
                            if result == dice_1:
                                dice_1 = 0
                            else:
                                dice_2 = 0
                        else:
                            # dubla
                            sum -= (result // dice_1)
                        print("=================")
            else:
                # mutare normala
                print(list_of_possible_move)
                while True:
                    try:
                        position = int(input("linia de unde muti "))
                        finish = int(input("linia la care pui "))
                    except ValueError:
                        print("NOT INTEGER")
                        continue
                    else:
                        break
                # print("decizie", finish)
                result = move_piece.move_piece(sit, sit.white, list_of_possible_move, position, finish)
                # print("res", result)
                if isinstance(result, bool):
                    print("Nu merge")
                else:
                    if dice_1 != dice_2:
                        if finish != -1:
                            if result == dice_1:
                                dice_1 = 0
                                sum -= 1
                            elif result == dice_2:
                                dice_2 = 0
                                sum -= 1
                            else:
                                print("WTF")
                        else:
                            if result == dice_1:
                                dice_1 = 0
                                sum -= 1
                            elif result == dice_2:
                                dice_2 = 0
                                sum -= 1
                            else:
                                x = max(dice_1, dice_2)
                                sum -= 1
                                if x == dice_1:
                                    dice_1 = 0
                                else:
                                    dice_2 = 0
                    else:
                        sum -= (result // dice_1)
        # print("CAP de finish")
