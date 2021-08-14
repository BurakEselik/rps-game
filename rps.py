#rock, paper, scissors game
from random import choice
import tkinter as tk

class Player:

    def __init__(self) -> None:
        pass

class Game:
    pass

class Rps(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Rock-Paper-Scissors GAME')


if __name__ == '__main__':
    rps = Rps()
    rps.mainloop()