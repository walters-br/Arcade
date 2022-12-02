class Score(): # keeps traack of score, every class will inherit it's score keep properties   
    def __init__(self,player1,player2) -> None:
       self.player1 = player1
       self.player2 = player2


# Each instance of any below game assumes 2 players 

class RPS(Score): # rock paper scissors
    def show(self):
     pass

class madlibs(Score): #madlibs game, gives player 1 or 2 a score if the other finds it funny
    def show(self):
     pass

class Hangman(Score):  # hangman game 
    def show(self):
     pass

class TwentyOneQuestions(Score): # twenty one questions game 
    def show(self):
     pass

class HeadsOrTails:  # each player bets on heads or tail 
    def show(self):
     pass

class NumGuesserGame:  # get x amount of guesses, with one player choosing to guess
    def show(self):
     pass 

class TikTakToe: # potential tik tac toe game
    def show(self):
     pass


