class Score(): # keeps traack of score, every class will inherit it's score keep properties   
    def __init__(self,player1,player2) -> None:
       self.player1 = player1  # name of player 1 
       self.player2 = player2  # name of player 2 
    
    def scorecount(x):# each class needs a way to store score and return it 
        pass 

# Each instance of any below game assumes 2 players 

class RPS(Score): # rock paper scissors
    def __init__(self):
     pass

class madlibs(Score): #madlibs game, gives player 1 or 2 a score if the other finds it funny
    def __init__(self,player1,player2):
        super().__init__(player1,player2) # gets player names from Score patent class
        pass 

class Hangman(Score):  # hangman game 
    def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 


class TwentyOneQuestions(Score): # twenty one questions game 
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 


class HeadsOrTails(Score):  # each player bets on heads or tail 
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 


class NumGuesserGame(Score):  # get x amount of guesses, with one player choosing to guess
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 

class TikTakToe(Score): # potential tik tac toe game
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 



