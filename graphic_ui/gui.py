import random
import tkinter as tk
from copy import deepcopy
from tkinter import messagebox

import logic_of_game.fortune
from logic_of_game import backgammon, math_moves, move_piece


class GUI:
    def __init__(self, main_window):
        """
        Initializes the Graphic User Interface and additional variables
        :param main_window: tkinter window
        """
        self.backgammon_frame = None
        self.control_frame = None
        self.dice_frame = None
        self.roll_button = None
        self.dice_label = None
        self.info_frame = None
        self.info_label = None
        self.turn_frame = None
        self.turn_label = None
        self.table_canvas = None
        self.backgammon = backgammon.Backgammon()
        self.main_window = main_window
        self.main_window.title("Backgammon")
        self.main_window.geometry("1000x600")
        self.create_menu()
        self.dices = None
        self.must_put_white = False
        self.must_put_black = False
        self.tura = None
        self.entry_label1 = None
        self.entry_value1 = None
        self.entry_label2 = None
        self.entry_value2 = None
        self.take_values_button = None
        self.value_frame = None
        self.round = 0
        self.ai_white = False
        self.ai_black = False
        self.information_move_ai = ""

    def reset_data(self):
        """
        reset G.U.I. for a new game
        :return: nothing
        """
        self.backgammon.reset()
        self.dices = [0, 0]
        self.must_put_white = False
        self.must_put_black = False
        self.round = 0
        self.ai_white = False
        self.ai_black = False
        self.tura = "NEGRU" if logic_of_game.fortune.decides_who_start() else "ALB"
        self.information_move_ai = ""

    def create_menu(self):
        """
        Create a menu for selecting type of game
        :return: nothing
        """
        menu_bar = tk.Menu(self.main_window)
        self.main_window.config(menu=menu_bar)
        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="MENIU", menu=game_menu)
        game_menu.add_command(label="OM vs OM", command=self.start_human_vs_human)
        game_menu.add_command(label="OM vs KOMPUTER", command=self.start_human_vs_ai)
        game_menu.add_separator()
        game_menu.add_command(label="EXIT", command=self.quit_game)

    def start_human_vs_human(self):
        """
        Start human vs human game
        Reset data from precedent game
        Build interface
        :return: nothing
        """
        self.reset_data()
        print(self.dices)
        self.build_infrastructure()

    def draw_table(self, frame_table):
        """
        Draw backgammon table
        :param frame_table: where to draw table
        :return: nothing
        """
        self.table_canvas = tk.Canvas(frame_table, width=600, height=600, bg="coral")
        for i in range(12):
            x = 600 - ((i + 1) * 50)
            y = 0
            if i in [j for j in range(0, 6)]:
                self.table_canvas.create_rectangle(x, y, x + 50, y + 50, outline='black', fill='gray90')
                self.table_canvas.create_text(x + 25, y + 30, text=str(i),
                                              font=("Press Start 2P", 15), fill='black')
            else:
                self.table_canvas.create_rectangle(x, y, x + 50, y + 50, outline='black', fill='chocolate4')
                self.table_canvas.create_text(x + 25, y + 30, text=str(i),
                                              font=("Press Start 2P", 15), fill='white')
            if i % 2 == 0:
                self.table_canvas.create_rectangle(x, y + 50, x + 50, y + 200, outline='black', fill='darkgoldenrod')
            else:
                self.table_canvas.create_rectangle(x, y + 50, x + 50, y + 200, outline='black', fill='chocolate3')
            if self.backgammon.tabla[i] < 0:
                self.table_canvas.create_text(x + 25, y + 125, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='gray20')
            if self.backgammon.tabla[i] > 0:
                self.table_canvas.create_text(x + 25, y + 125, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='gray90')
        for i in range(12, 24):
            x = 0 + ((i - 12) * 50)
            y = 375
            if i in [j for j in range(18, 24)]:
                self.table_canvas.create_rectangle(x, y + 150, x + 50, y + 200, outline='black', fill='gray20')
                self.table_canvas.create_text(x + 25, y + 180, text=str(i),
                                              font=("Press Start 2P", 15), fill='white')
            else:
                self.table_canvas.create_rectangle(x, y + 150, x + 50, y + 200, outline='black', fill='chocolate4')
                self.table_canvas.create_text(x + 25, y + 180, text=str(i),
                                              font=("Press Start 2P", 15), fill='white')

            if i % 2 == 0:
                self.table_canvas.create_rectangle(x, y, x + 50, y + 150, outline='black', fill='darkgoldenrod')
            else:
                self.table_canvas.create_rectangle(x, y, x + 50, y + 150, outline='black', fill='chocolate3')
            if self.backgammon.tabla[i] < 0:
                self.table_canvas.create_text(x + 25, y + 75, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='gray20')
            if self.backgammon.tabla[i] > 0:
                self.table_canvas.create_text(x + 25, y + 75, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='gray90')
        self.table_canvas.pack(side="left")

    def build_table(self):
        """
        Build backgammon table
        :return: nothing
        """
        self.backgammon_frame = tk.Frame(self.main_window)
        self.backgammon_frame.pack(side=tk.LEFT)
        self.draw_table(self.backgammon_frame)

    def build_control_frame(self):
        """
        Build control frame where will be widgets
        :return: nothing
        """
        self.control_frame = tk.Frame(self.main_window)
        self.control_frame.pack()

    def build_dice_frame(self):
        """
        Build dice frame where will be displayed dices and button to generate new set of dices
        :return:
        """
        self.dice_frame = tk.Frame(self.control_frame, width=400, height=100)
        self.dice_frame.pack(side=tk.TOP, pady=5)

    def build_insert_value(self):
        """
        Build frame for inserting input for moving pieces on table,
        but in AI mode will display a button for confirm AI moves
        :return: nothing
        """
        if self.round > 0:
            self.value_frame = tk.Frame(self.control_frame, width=400, height=200)
            self.value_frame.pack(side=tk.BOTTOM, pady=5)
            if (self.tura == "ALB" and not self.must_put_white) or (self.tura == "NEGRU" and not self.must_put_black):
                print("HI")
                self.entry_label1 = tk.Label(self.value_frame, text="De unde muti?:", font=("Press Start 2P", 8))
                self.entry_label1.grid(row=0, column=0, pady=5)
                self.entry_value1 = tk.Entry(self.value_frame, font=("Consolas", 12))
                self.entry_value1.grid(row=0, column=1, pady=5)
                self.entry_label2 = tk.Label(self.value_frame, text="Unde muti?:", font=("Press Start 2P", 8))
                self.entry_label2.grid(row=1, column=0, padx=2.5, pady=5)
                self.entry_value2 = tk.Entry(self.value_frame, font=("Consolas", 12))
                self.entry_value2.grid(row=1, column=1, padx=2.5, pady=5)
            else:
                print("AICI")
                self.entry_label1 = tk.Label(self.value_frame, text="Unde pui?:", font=("Press Start 2P", 8))
                self.entry_label1.grid(row=0, column=0, pady=5)
                self.entry_value1 = tk.Entry(self.value_frame, font=("Consolas", 12))
                self.entry_value1.grid(row=0, column=1, pady=5)
            self.take_values_button = tk.Button(self.value_frame, text="Muta", command=self.take_values,
                                                font=("Press Start 2P", 10))
            self.take_values_button.grid(row=2, column=0, columnspan=2, pady=5)
        if self.round == -1:
            self.value_frame = tk.Frame(self.control_frame, width=400, height=200)
            self.value_frame.pack(side=tk.BOTTOM, pady=5)
            self.take_values_button = tk.Button(self.value_frame, text="Confirm", command=self.confirm,
                                                font=("Press Start 2P", 10))
            self.take_values_button.grid(row=0, column=0, columnspan=2, pady=5)

    def confirm(self):
        """
        Prepare variables for human player
        :return: nothing
        """
        self.round = 0
        self.dices = [0, 0]
        self.tura = "NEGRU" if self.tura == "ALB" else "ALB"
        self.build_infrastructure()

    def build_roll_button(self):
        """
        Build roll button if is situation for that
        Or
        Display moves made by AI
        Or
        Display number of moves for human player
        :return: nothing
        """
        if self.round == 0:
            self.roll_button = tk.Button(self.dice_frame, text="DA-I CU ZARUL",
                                         command=self.roll_dice,
                                         font=("Press Start 2P", 14))
            self.roll_button.pack(anchor=tk.CENTER, expand=True, padx=5, pady=5)
        elif self.round == -1:
            self.roll_button = tk.Label(self.dice_frame, text=self.information_move_ai,
                                        font=("Press Start 2P", 10))
            self.roll_button.pack(anchor=tk.CENTER, expand=True, padx=5, pady=5)
        else:
            self.roll_button = tk.Label(self.dice_frame, text="MUTARI DE FACUT " + str(self.round),
                                        font=("Press Start 2P", 10))
            self.roll_button.pack(anchor=tk.CENTER, expand=True, padx=5, pady=5)

    def build_dice_label(self):
        """
        Display dices
        :return: nothing
        """
        string_phrase = "NULL" if self.dices == [0, 0] else str(self.dices[0]) + "  " + str(self.dices[1])
        self.dice_label = tk.Label(self.dice_frame, text="ZARURI DATE = " + string_phrase, font=("Press Start 2P", 12))
        self.dice_label.pack(padx=5, pady=5)

    def build_info_frame(self):
        """
        Build frame for information section
        :return: nothing
        """
        self.info_frame = tk.Frame(self.control_frame, width=400, height=200, bd=5)
        self.info_frame.pack(side=tk.BOTTOM, pady=5)

    def build_info_label(self):
        """
        Display information about status of game
        :return: nothing
        """
        string_info = "RETRASE ALB : " + str(self.backgammon.white_set) + "\n"
        string_info += "RETRASE NEGRU : " + str(self.backgammon.black_set) + "\n"
        string_info += "SCOASE ALB : " + str(self.backgammon.remove_white) + "\n"
        string_info += "SCOASE NEGRU : " + str(self.backgammon.remove_black)
        self.info_label = tk.Label(self.info_frame, text=string_info, font=("Press Start 2P", 14))
        self.info_label.pack()

    def build_turn_frame(self):
        """
        Build frame for displaying what player move
        :return: nothing
        """
        self.turn_frame = tk.Frame(self.control_frame, width=400, height=150)
        self.turn_frame.pack(side=tk.BOTTOM)

    def build_turn_label(self):
        """
        Display what player move
        :return: nothing
        """
        message = self.tura
        if (self.ai_white and self.tura =="ALB") or (self.ai_black and self.tura == "NEGRU"):
            message += " [A.I.]"
        self.turn_label = tk.Label(self.turn_frame, text="TURA: " + message, font=("Press Start 2P", 14))
        self.turn_label.pack()

    def build_infrastructure(self):
        """
        Build graphic interface or displaing a message when a player win
        :return: nothing
        """
        print(self.backgammon)
        decision = self.backgammon.win_what()
        if isinstance(decision, bool):
            for widget in self.main_window.winfo_children():
                widget.destroy()
            self.create_menu()
            self.build_table()
            self.build_control_frame()
            self.build_dice_frame()
            self.build_roll_button()
            self.build_dice_label()
            self.build_info_frame()
            self.build_info_label()
            self.build_turn_frame()
            self.build_turn_label()
            self.build_insert_value()
            print(self.dices)
            print(self.round)
        else:
            if decision == 1:
                messagebox.showinfo("CASTIGATOR", "JUCATORUL ALB A CASTIGAT")
            else:
                messagebox.showinfo("CASTIGATOR", "JUCATORUL NEGRU A CASTIGAT")

    def start_human_vs_ai(self):
        """
        Start human vs AI game
        Reset data from precedent game
        Decides what player is AI
        Build interface
        :return: nothing
        """
        self.reset_data()
        if logic_of_game.fortune.decides_who_start():
            self.ai_black = True
            print("NEGRU AI")
        else:
            self.ai_white = True
            print("ALB AI")
        self.build_infrastructure()

    def roll_dice(self):
        """
        Simulating roll the dices
        Calculate the rounds
        Call update_dice_label()
        :return: nothing
        """
        if self.round == 0:
            dices_s = logic_of_game.fortune.dices()
            # print(dices_s)
            self.dices = dices_s
            if dices_s[0] == dices_s[1]:
                self.round = 4
            else:
                self.round = 2
            self.update_dice_label()

    def update_dice_label(self):
        """
        Rebuild interface
        If is in human_vs_ai, call AI method to move pieces
        :return: nothing
        """
        player = 1 if self.tura == "ALB" else -1
        if (player == 1 and self.ai_white) or (player == -1 and self.ai_black):
            self.move_ai()
        self.build_infrastructure()

    def take_values(self):
        """
        Take values from moving a piece for human player
        Call method for moving piece in backgammon table
        :return: nothing
        """
        try:
            if (self.tura == "ALB" and not self.must_put_white) or (self.tura == "NEGRU" and not self.must_put_black):
                value1 = int(self.entry_value1.get())
                value2 = int(self.entry_value2.get())
                print("Value 1:", value1)
                print("Value 2:", value2)
                if value1 < -1 or value1 > 24 or value2 < -1 or value2 > 24:
                    messagebox.showerror("Eroare", "Va rugam sa furnizati numere intre -1 si 23")
                self.move_from_to(value1, value2)
            else:
                value1 = int(self.entry_value1.get())
                print("Value 1:", value1)
                if value1 < -1 or value1 > 24:
                    messagebox.showerror("Eroare", "Va rugam sa furnizati numere intre -1 si 23")
                self.put_piece(value1)

        except ValueError:
            messagebox.showerror("Eroare", "Numere intregi va rugam.")

    def put_piece(self, value_1):
        """
        Place a removed piece on table
        Call build_infrastructure() to refresh interface
        :param value_1: where place the piece
        :return: nothing
        """
        player = 1 if self.tura == "ALB" else -1
        print("player", player)
        list_of_possibles = math_moves.where_can_place_piece(self.backgammon, player, self.dices[0], self.dices[1])
        print(list_of_possibles)
        if len(list_of_possibles) == 0:
            messagebox.showinfo("Informatie", "NU PUTETI MUTA")
            self.round = 0
            self.dices = [0, 0]
            self.tura = "NEGRU" if player == 1 else "ALB"
            self.build_infrastructure()
        else:
            _to = value_1
            if _to not in list_of_possibles:
                messagebox.showinfo("Informatie", "NU AI CUM SA PUI PIESA ACOLO")
            else:
                result = move_piece.move_piece_on_table(self.backgammon, player, list_of_possibles, _to)
                print("result", result)
                if isinstance(result, bool):
                    messagebox.showinfo("Informatie", "CEVA O MERS PROST")
                else:
                    if self.dices[0] != self.dices[1]:
                        self.round -= 1
                        if result == self.dices[0]:
                            self.dices[0] = 0
                        else:
                            self.dices[1] = 0
                    else:
                        self.round -= (result // self.dices[1])
            if self.round == 0:
                self.tura = "NEGRU" if player == 1 else "ALB"
            if self.backgammon.remove_white == 0:
                self.must_put_white = False
            else:
                self.must_put_white = True
            if self.backgammon.remove_black == 0:
                self.must_put_black = False
            else:
                self.must_put_black = True
            self.build_infrastructure()

    def move_from_to(self, value1, value2):
        """
            Move piece on backgammon table
            Call build_infrastructure() to refresh interface
            :param value1: from what place move piece
            :param value2: where we move piece
            :return: nothing
            """
        player = 1 if self.tura == "ALB" else -1
        print("player", player)
        if self.dices[0] != self.dices[1]:
            list_move = math_moves.available_move(self.backgammon, player, self.dices[0], self.dices[1])
        else:
            list_move = math_moves.available_move(self.backgammon, player, self.dices[0], self.dices[1], self.round)
        if len(list_move) == 0:
            messagebox.showinfo("Informatie", "NU PUTETI MUTA")
            self.round = 0
            self.dices = [0, 0]
            self.tura = "NEGRU" if player == 1 else "ALB"
            self.build_infrastructure()
        else:
            print(list_move)
            _from = value1
            _to = value2

            if _from not in list_move.keys():
                messagebox.showinfo("Informatie", "NU AI PIESE ACOLO")
            elif _to not in list_move[_from]:
                messagebox.showinfo("Informatie", "NU AI CUM SA MUTI ACOLO")
            else:
                result = move_piece.move_piece(self.backgammon, player, list_move, _from, _to)
                if isinstance(result, bool):
                    messagebox.showinfo("Informatie", "CEVA O MERS PROST")
                else:
                    print("result", result)
                    if self.dices[0] != self.dices[1]:
                        if _to != -1:
                            if result == self.dices[0]:
                                self.dices[0] = 0
                                self.round -= 1
                            elif result == self.dices[1]:
                                self.dices[1] = 0
                                self.round -= 1
                            else:
                                messagebox.showinfo("Informatie", "CEVA O MERS PROST")
                        else:
                            if result == self.dices[0]:
                                self.dices[0] = 0
                                self.round -= 1
                            elif result == self.dices[1]:
                                self.dices[1] = 0
                                self.round -= 1
                            else:
                                x = max(self.dices[0], self.dices[1])
                                self.round -= 1
                                if x == self.dices[0]:
                                    self.dices[0] = 0
                                else:
                                    self.dices[1] = 0
                    else:
                        self.round -= 1
            if self.round == 0:
                self.tura = "NEGRU" if player == 1 else "ALB"
            if self.backgammon.remove_white == 0:
                self.must_put_white = False
            else:
                self.must_put_white = True
            if self.backgammon.remove_black == 0:
                self.must_put_black = False
            else:
                self.must_put_black = True
            self.build_infrastructure()

    def move_ai(self):
        """
        Method for AI player to play the game
        :return: nothing
        """
        dices = deepcopy(self.dices)
        self.information_move_ai = ""
        player = 1 if self.tura == "ALB" else -1
        while self.round != 0:
            if (player == 1 and self.backgammon.remove_white != 0) or (
                    player == -1 and self.backgammon.remove_black != 0):
                list_of_moves = math_moves.where_can_place_piece(self.backgammon, player, dices[0], dices[1])
                if len(list_of_moves) == 0:
                    self.round = 0
                    self.information_move_ai += "NU A PUTUT PUNE PIESA"
                else:
                    where_place = random.choice(list_of_moves)
                    print(where_place)
                    result = move_piece.move_piece_on_table(self.backgammon, player, list_of_moves, where_place)
                    print("result", result)
                    if isinstance(result, bool):
                        print("Nu merge")
                        break
                    else:
                        if dices[0] != dices[1]:
                            # normal
                            self.round -= 1
                            if result == dices[0]:
                                dices[0] = 0
                            else:
                                dices[1] = 0
                        else:
                            # dubla
                            self.round -= 1
                        self.information_move_ai += "PUS LA POZITIA "
                        self.information_move_ai += str(where_place)
                        self.information_move_ai += "\n"
            else:
                if dices[0] != dices[1]:
                    list_of_moves = math_moves.available_move(self.backgammon, player, dices[0], dices[1])
                else:
                    list_of_moves = math_moves.available_move(self.backgammon, player, dices[0], dices[1], self.round)
                if len(list_of_moves) == 0:
                    self.round = 0
                    self.information_move_ai += "NU A PUTUT PUNE PIESA"
                else:
                    _from = random.choice(list(list_of_moves.keys()))
                    _to = random.choice(list_of_moves[_from])
                    print(_from, " ", _to)
                    result = move_piece.move_piece(self.backgammon, player, list_of_moves, _from, _to)
                    print("result", result)
                    if isinstance(result, bool):
                        print("Nu merge")
                        break
                    else:
                        if dices[0] != dices[1]:
                            if _to != -1:
                                if result == dices[0]:
                                    dices[0] = 0
                                    self.round -= 1
                                elif result == dices[1]:
                                    dices[1] = 0
                                    self.round -= 1
                                else:
                                    messagebox.showinfo("Informatie", "CEVA O MERS PROST")
                            else:
                                if result == dices[0]:
                                    dices[0] = 0
                                    self.round -= 1
                                elif result == dices[1]:
                                    dices[1] = 0
                                    self.round -= 1
                                else:
                                    x = max(dices[0], dices[1])
                                    self.round -= 1
                                    if x == dices[0]:
                                        dices[0] = 0
                                    else:
                                        dices[1] = 0
                        else:
                            self.round -= 1
                        self.information_move_ai += "MUTAT "
                        self.information_move_ai += str(_from) + " => " + str(_to)
                        self.information_move_ai += "\n"
        if self.backgammon.remove_white == 0:
            self.must_put_white = False
        else:
            self.must_put_white = True
        if self.backgammon.remove_black == 0:
            self.must_put_black = False
        else:
            self.must_put_black = True
        self.round = -1

    def quit_game(self):
        """
        Close the window and quit the game
        :return: nothing
        """
        self.main_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    menu = GUI(root)
    root.mainloop()
