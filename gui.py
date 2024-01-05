import time
import tkinter as tk
from tkinter import messagebox

import tui_game.fortune
from tui_game import backgammon, move_piece
from tui_game import math_moves


class GUI:
    def __init__(self, root):
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
        self.root = root
        self.root.title("Backgammon")
        self.root.geometry("1000x600")
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

    def reset_data(self):
        self.backgammon = backgammon.Backgammon()
        self.dices = None
        self.must_put_white = False
        self.must_put_black = False
        self.round = 0
        self.tura = "NEGRU" if tui_game.fortune.decides_who_start() else "ALB"

    def create_menu(self):
        # Menu Bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Game Menu
        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="MENIU", menu=game_menu)
        game_menu.add_command(label="OM vs OM", command=self.start_human_vs_human)
        game_menu.add_command(label="OM vs KOMPUTER", command=self.start_human_vs_ai)
        game_menu.add_separator()
        game_menu.add_command(label="EXIT", command=self.quit_game)

    def start_human_vs_human(self):
        self.reset_data()
        print(self.dices)
        # Add your code to start a human vs AI game here
        self.build_infrastructure()

    def draw_table(self, frame_table):
        self.table_canvas = tk.Canvas(frame_table, width=600, height=600, bg="coral")

        for i in range(12):
            x = 600 - ((i + 1) * 50)
            y = 0
            self.table_canvas.create_rectangle(x, y, x + 50, y + 50, outline='black', fill='chocolate4')
            self.table_canvas.create_text(x + 25, y + 30, text=str(i),
                                          font=("Press Start 2P", 15), fill='white')
            if i % 2 == 0:
                self.table_canvas.create_rectangle(x, y + 50, x + 50, y + 200, outline='black', fill='darkgoldenrod')
            else:
                self.table_canvas.create_rectangle(x, y + 50, x + 50, y + 200, outline='black', fill='chocolate3')
            if self.backgammon.tabla[i] < 0:
                self.table_canvas.create_text(x + 25, y + 125, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='black')
            if self.backgammon.tabla[i] > 0:
                self.table_canvas.create_text(x + 25, y + 125, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='white')
        for i in range(12, 24):
            x = 0 + ((i - 12) * 50)
            y = 375
            self.table_canvas.create_rectangle(x, y + 150, x + 50, y + 200, outline='black', fill='chocolate4')
            self.table_canvas.create_text(x + 25, y + 180, text=str(i),
                                          font=("Press Start 2P", 15), fill='white')
            if i % 2 == 0:
                self.table_canvas.create_rectangle(x, y, x + 50, y + 150, outline='black', fill='darkgoldenrod')
            else:
                self.table_canvas.create_rectangle(x, y, x + 50, y + 150, outline='black', fill='chocolate3')
            if self.backgammon.tabla[i] < 0:
                self.table_canvas.create_text(x + 25, y + 75, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='black')
            if self.backgammon.tabla[i] > 0:
                self.table_canvas.create_text(x + 25, y + 75, text=str(abs(self.backgammon.tabla[i])),
                                              font=("Press Start 2P", 20), fill='white')

        self.table_canvas.pack(side="left")

    def build_table(self):
        self.backgammon_frame = tk.Frame(self.root)
        self.backgammon_frame.pack(side=tk.LEFT)
        self.draw_table(self.backgammon_frame)

    def build_control_frame(self):
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

    def build_dice_frame(self):
        self.dice_frame = tk.Frame(self.control_frame, width=400, height=100)
        self.dice_frame.pack(side=tk.TOP, pady=5)

    def build_insert_value(self):
        if self.round != 0:
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
            # Add Button to take the values
            self.take_values_button = tk.Button(self.value_frame, text="Muta", command=self.take_values,
                                                font=("Press Start 2P", 10))
            self.take_values_button.grid(row=2, column=0, columnspan=2, pady=5)

    def build_roll_button(self):
        if self.round == 0:
            self.roll_button = tk.Button(self.dice_frame, text="DA-I CU ZARUL",
                                         command=lambda: self.roll_dice(self.dice_label),
                                         font=("Press Start 2P", 14))
            self.roll_button.pack(anchor=tk.CENTER, expand=True, padx=5, pady=5)
        else:
            self.roll_button = tk.Label(self.dice_frame, text="MUTARI DE FACUT " + str(self.round),
                                        font=("Press Start 2P", 10))
            self.roll_button.pack(anchor=tk.CENTER, expand=True, padx=5, pady=5)

    def build_dice_label(self):
        string_phrase = "NULL" if self.dices is None else str(self.dices[0]) + "  " + str(self.dices[1])
        self.dice_label = tk.Label(self.dice_frame, text="ZARURI DATE = " + string_phrase, font=("Press Start 2P", 12))
        self.dice_label.pack(padx=5, pady=5)

    def build_info_frame(self):
        self.info_frame = tk.Frame(self.control_frame, width=400, height=200, bd=5)
        self.info_frame.pack(side=tk.BOTTOM, pady=5)

    def build_info_label(self):
        string_info = "RETRASE ALB : " + str(self.backgammon.white_set) + "\n"
        string_info += "RETRASE NEGRU : " + str(self.backgammon.black_set) + "\n"
        string_info += "SCOASE ALB : " + str(self.backgammon.remove_white) + "\n"
        string_info += "SCOASE NEGRU : " + str(self.backgammon.remove_black)
        self.info_label = tk.Label(self.info_frame, text=string_info, font=("Press Start 2P", 14))
        self.info_label.pack()

    def build_turn_frame(self):
        self.turn_frame = tk.Frame(self.control_frame, width=400, height=150)
        self.turn_frame.pack(side=tk.BOTTOM)

    def build_turn_label(self):
        self.turn_label = tk.Label(self.turn_frame, text="TURA: " + self.tura, font=("Press Start 2P", 14))
        self.turn_label.pack()

    def build_infrastructure(self):
        print(self.backgammon)
        decision = self.backgammon.win_what()
        if isinstance(decision, bool):
            for widget in self.root.winfo_children():
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
        self.reset_data()
        self.build_infrastructure()

    def roll_dice(self, dice_label):
        if self.round == 0:
            dices_s = tui_game.fortune.dices()
            # print(dices_s)
            self.dices = dices_s
            if dices_s[0] == dices_s[1]:
                self.round = 4
            else:
                self.round = 2
            self.update_dice_label(dice_label)

    def update_dice_label(self, dice_label):
        self.build_infrastructure()

    def take_values(self):
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
            # Do something with the values, e.g., print them

        except ValueError:
            messagebox.showerror("Eroare", "Numere intregi va rugam.")

    def put_piece(self, value_1):
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
            if self.backgammon.remove_black == 0:
                self.must_put_black = False
            self.build_infrastructure()

    def move_from_to(self, value1, value2):
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
                                dice_1 = 0
                                self.round -= 1
                            elif result == self.dices[1]:
                                dice_2 = 0
                                self.round -= 1
                            else:
                                x = max(self.dices[0], self.dices[1])
                                self.round -= 1
                                if x == self.dices[0]:
                                    self.dices[0] = 0
                                else:
                                    self.dices[1] = 0
                    else:
                        self.round -= (result // self.dices[1])
            if self.round == 0:
                self.tura = "NEGRU" if player == 1 else "ALB"
            if self.backgammon.remove_white != 0:
                self.must_put_white = True
            if self.backgammon.remove_black != 0:
                self.must_put_black = True
            self.build_infrastructure()

    def quit_game(self):
        # Add your code to handle quitting the game here
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    menu = GUI(root)
    root.mainloop()
