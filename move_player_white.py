import backgammon as bk
import fortune as frt
import math_moves
import move_piece


def move_white(sit: bk.Backgammon):
    dice_1, dice_2 = frt.dices()
    if dice_1 != dice_2:
        sum = dice_1 + dice_2
        round = None
    else:
        sum = 4 * dice_1
        round = 4

    while sum != 0:
        if dice_1 != dice_2:
            list_of_possible_move = math_moves.available_move(sit, sit.white, dice_1, dice_2)
        else:
            list_of_possible_move = math_moves.available_move(sit, sit.white, dice_1, dice_2, round)
        if len(list_of_possible_move) == 0:
            print("BLOCAJ")
            return -1
        if sit.remove_white != 0:
            # inseamna ca trebuie sa pun piesa pe tabla in casa adversarului
            list_of_possible_move_on_adversary = math_moves.where_can_place_piece(sit, sit.white)
            if len(list_of_possible_move_on_adversary) == 0:
                print("BLOCAJ")
                return -1
            else:
                print(list_of_possible_move_on_adversary)
                finish = int(input("linia unde pui piesa"))
                result = move_piece.move_piece_on_table(sit, sit.white, list_of_possible_move_on_adversary, finish)
                if result == False:
                    print("Nu merge")
                else:
                    print(result)
                    sum -= result
                    if dice_1 != dice_2:
                        dice_1 = 0
                    else:
                        round -= (result // dice_1)
