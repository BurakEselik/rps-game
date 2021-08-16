# rock, paper, scissors game
from random import choice
import tkinter as tk
import tkinter.messagebox as msgbox


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
            raise ValueError(
                f'Just {self.hands}, given: {str(value[:10]) if len(value) > 10 else str(value)}...')

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
        '''compare the hands of the instances'''

        if self.hand == o.hand:
            return False
        elif self.hand == self.hands[0] and o.hand == self.hands[1]:
            return False
        elif self.hand == self.hands[1] and o.hand == self.hands[2]:
            return False
        elif self.hand == self.hands[2] and o.hand == self.hands[0]:
            return False
        else:
            return True

    def __lt__(self, o: object) -> bool:
        '''compare the hands of the instances'''

        if self.hand == o.hand:
            return False
        elif self.hand == self.hands[0] and o.hand == self.hands[1]:
            return True
        elif self.hand == self.hands[1] and o.hand == self.hands[2]:
            return True
        elif self.hand == self.hands[2] and o.hand == self.hands[0]:
            return True
        else:
            return False


class Game:

    def __init__(self) -> None:
        ''' When Game class lanches then creats 2 player '''
        self.user_player = Player('user_player')
        self.cpu_player = Player('cpu_player')

    def __computer_ent_handling(self, hand):
        self.ent_comp_player.delete(0, tk.END)
        self.ent_comp_player.insert(0, hand)

    def play(self):
        ''' Game Play Method '''
        try:
            self.user_player.hand = str(self.ent_user_player.get()).lower()  
        except ValueError:
            msgbox.showinfo("Hey hey", 'Please just type: rock, paper or scissors')
            return None
        self.cpu_player.hand = choice(self.cpu_player.hands)

        if self.user_player == self.cpu_player:

            self.__computer_ent_handling(self.cpu_player.hand)
            self.lbl_result.config(text ='This round is equal')
        elif self.user_player > self.cpu_player:
            self.__computer_ent_handling(self.cpu_player.hand)
            self.lbl_result.config(text ='You won this round')
            self.user_player + 1
            if self.check_score(self.user_player):
                if msgbox.askyesno('You Won!', 'Do you want to play again?'):
                    self.user_player.score, self.cpu_player.score = 0, 0
                    return self.reset()
                else: 
                    return self.exitt()
        elif self.user_player < self.cpu_player:
            self.__computer_ent_handling(self.cpu_player.hand)
            self.lbl_result.config(text ='computer won this round')
            self.cpu_player + 1
            if self.check_score(self.cpu_player):
                if msgbox.askyesno('Game Over - Cpu Won', 'Do you want to play again?'):
                    self.user_player.score, self.cpu_player.score = 0, 0
                    return self.reset()
                else: 
                    return self.exitt()
        else:
            pass

    def reset(self):
        self.lbl_result.config(text ='')
        self.ent_comp_player.delete(0, tk.END)
        self.ent_user_player.delete(0, tk.END)

    def exitt(self):
        self.title('Good by!')
        self.after(500, self.destroy)

    def check_score(self, o: object) -> bool:
        ''' Returns if score reached 3 that given object '''
        if o.score == 3:
            return True
        else: return False


class Rps(tk.Tk, Game):

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        Game.__init__(self)

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

        self.btn_for_play = tk.Button(text="PLAY",
                                      width=10,
                                      height=2,
                                      command=self.play
                                      )

        self.btn_for_play.place(x=215, y=100)

        self.lbl_result = tk.Label(
            text=' ', bg='black', fg='white', width=30)
        self.lbl_result.place(x=150, y=160)

        self.btn_exit = tk.Button(text='Exit', command=self.exitt)
        self.btn_exit.place(x=160, y=200)

        self.btn_reset = tk.Button(text='Reset', command=self.reset)
        self.btn_reset.place(x=320, y=200)


if __name__ == '__main__':
    rps = Rps()
    rps.mainloop()
