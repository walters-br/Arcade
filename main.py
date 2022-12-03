import random
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
    
    
    while True:
     player1input= input("Player One Choose Rock,Paper,or Scissors\n")
     player2input = input("Player Two Choose Rock,Paper,or Scissors\n")
     
     if player1input == player2input: 
        print(f"It's a draw, both players selected",{player2input})
     
     elif player1input == "Rock": 
            if player2input=="Scissors":
                print("Player One wins, Rock beats Scissors")   # add class specific object here 
            else: 
                print("Plater 2 wins Paper Covers Rock")
     
     
     elif player1input == "Scissors":
            if player2input == "Rock":
                print("Player 2 wins, Rock beats Scissors")   # add class specific object here 
            else: 
                print("Plater 1 wins, Scissors cuts paper")

     
     elif player1input == "Paper": 
         if player2input =="Rock":
                print("Player One wins, Paper beats Rock")   # add class specific object here 
         else: 
                print("Plater 2 wins, Scissors beats Paper")

     Continue = input('Play againz?(y/n):')    # unit test 
     if Continue == 'y': 
        break 
     else: 
        continue 



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
        while True: 
          answer = random.randint(1,2)  # turn into a method 
          player1_guess = int(" Plater 1, State your guess H or T")
          player2_guess = int(" Plater 1, State your guess H or T")
          
          if player1_guess == "H": 
                player1_guess=0 
          if player2_guess == "H": 
                player2_guess=0
         

          if player1_guess == "T": 
                player1_guess=1 
          if player2_guess == "T": 
                player2_guess=1
         
          if player1_guess == answer:
                 print('Player 1 guessed right, the answer was: ', answer)
          else: 
                 print('Player 2 guessed right, the answer was: ', answer)
        
          Continue = input('Play againz?(y/n):')    # unit test 
          if Continue == 'y': 
             break 




            
          
            
         





class NumGuesserGame(Score):  # get x amount of guesses, with one player choosing to guess
    
    def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 

class TikTakToe(Score): # potential tik tac toe game
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 



