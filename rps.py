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
    pass

class Rps(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Rock-Paper-Scissors GAME')


if __name__ == '__main__':
    #rps = Rps()
    #rps.mainloop()
    a = Player('a')
    b = Player('b')

    a.hand = 'rock'
    b.hand = 'rock'
    a + [1,2]
    print(a)
