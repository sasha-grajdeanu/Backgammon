from tui_game import game


def main():
    """
    Main function for Text-user interface of game
    :return: nothing
    """
    while True:
        what_game = int(input("What game would you like to (1 for hvh, 2 for hvAI): "))
        if what_game == 1:
            game.game_h_vs_h()
            break
        if what_game == 2:
            game.game_h_vs_ai()
            break
        else:
            print("OMG")


if __name__ == "__main__":
    main()
