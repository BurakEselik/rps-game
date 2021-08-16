#rock, paper, scissors game
from random import choice
import tkinter as tk

class Player:

    hands = ['rock', 'paper', 'scissors']
    SCORE = 0

    def __init__(self, name, score=SCORE) -> None:
        self.name = name
        self.__score_ = score
        self.__hand_ = None

    @property
    def score(self):
        return self.__score_

    @score.setter
    def score(self, value):
        self.__score_ = value

    @property
    def hand(self):
        return self.__hand_

    @hand.setter
    def hand(self, value):
        if value in self.hands:
            self.__hand_ = value
        else:
            raise ValueError(f'Just {self.hands}, given: {str(value)}')

    def __str__(self):
        return f'{self.name}: score is {self.score}, hand is {self.hand}'
    
    def __eq__(self, o: object) -> bool:
        '''compare the hands of the instances'''
        if (self.hand == o.hand):
            return True
        else:
            return False

    def __add__(self, o: object):
        '''add just 1 number for the instance'''
        if o == 1:
            self.score = self.score + o
        else:
            raise ValueError(f'Just int: 1, given: {str(o)}')

    def __gt__(self, o: object) -> bool:
        '''compare the scores of the instances'''
        if self.score > o.score:
            return True
        else:
            return False

    def __lt__(self, o: object) -> bool:
        '''compare the scores of the instances'''
        if self.score < o.score:
            return True
        else:
            return False

    


class Game:

    def __init__(self) -> None:

        pass

    def play(self):
        pass

class Rps(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Rock-Paper-Scissors GAME')
        self.resizable(width=False, height=False)
        self.geometry("550x250")
    

        self.lbl_user_player = tk.Label(self, text='YOU', fg='green')
        self.lbl_user_player.place(x=40, y=30)

        self.ent_user_player = tk.Entry(self, width=20)
        self.ent_user_player.place(x=40, y=55)

        self.lbl_comp_player = tk.Label(self, text='COMPUTER', fg='red')
        self.lbl_comp_player.place(x=420, y=30)

        self.ent_comp_player = tk.Entry(self, width=20)
        self.ent_comp_player.place(x=335, y=55) 

        self.btn_for_play = tk.Button(  text="PLAY",
                                        width=10,
                                        height=2,
                                        #bg="blue",
                                        #fg="yellow",
                                    )

        self.btn_for_play.place(x=215, y=100)

        self.lbl_result = tk.Label(text='test', bg='black', fg='white', width=30)
        self.lbl_result.place(x=150, y=160)

        self.btn_exit = tk.Button(text='Exit')
        self.btn_exit.place(x=160, y=200)

        self.btn_reset = tk.Button(text='Reset')
        self.btn_reset.place(x=320, y=200)


if __name__ == '__main__':
    rps = Rps()
    rps.mainloop()
