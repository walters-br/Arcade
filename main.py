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
     if Continue == 'n': 
        break 
     else: 
        continue 



class madlibs(Score): #madlibs game, gives player 1 or 2 a score if the other finds it funny
    def __init__(self,player1,player2):
        super().__init__(player1,player2) # gets player names from Score patent class
        pass 

class Hangman(Score):  # hangman game 
# hangman 
    intialize=True
    player1_win=0
    while intialize: 
        start = int(input('Welcome to Hangman. Which player wants to create a word (1 or 2)\n'))
    
        if start==1: 
            answer_string = input('Player 1 , enter a word of your choice. Make sure Player 2 is looking away. ')
            answer_string= answer_string.upper()
            num_of_guesses = 0
            attempts=[]
            word_display= "_" * len(answer_string)
            Win = 0
            print('Player 2, you have 6 tries to guess the word. Enter one letter at a time ')
            
        while num_of_guesses < 8 :
            guess=input('Player 2, please guess a letter').upper() # turns all guesses into uppercase form
            
            if len(guess)==1 and guess.isalpha(): # if player enters a letter and is a letter
                
                
                
                if guess not in answer_string:
                    print('Sorry,', guess,'is not in the word')
                    num_of_guesses +=1
                    print('You have ',6-num_of_guesses,' left.')
                    attempts.append(guess) # throws the guess into a list of previous guesses
                else:
                    print('Good choice' , guess, ' is in the word')
                    attempts.append(guess)
                    correct_attempts_display=list(word_display)
                    indices = [x for x, letter in enumerate(answer_string) if letter==guess]
                    for index in indices: 
                        correct_attempts_display[index]=guess
                        word_display=''.join(correct_attempts_display)
                    if '_' not in word_display: 
                        Win=1
            else:
                print('Not a valid guess')
            
            if Win==1:
                print('You guessed the word')
                player1_win+=1
                break
            elif num_of_guesses==6 :
                print('Sorry the word was',answer_string )
                break


    
    
    
    
    
    
    
    else: 
        answer_string2=input('Player 2, enter the word if your choice')

    
    

class TwentyOneQuestions(Score): # twenty one questions game 
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        pass 








class HeadsOrTails(Score):  # each player bets on heads or tail 
   
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        while True: 
          answer = random.randint(1,2)  # turn into a method 
          player1_guess = input(" Plater 1, State your guess H or T")
          player2_guess = input(" Plater 1, State your guess H or T")
          
          if player1_guess == "H": 
                player1_guess=1 
          if player2_guess == "H": 
                player2_guess=1
         

          if player1_guess == "T": 
                player1_guess=2 
          if player2_guess == "T": 
                player2_guess=2
         
          if player1_guess == answer:
                 print('Player 1 guessed right, the answer was: ', answer)
          else: 
                 print('Player 2 guessed right, the answer was: ', answer)
        
          Continue = input('Play againz?(y/n):')    # unit test 
          if Continue == 'y': 
             continue 
          else:
            break




            
          
            
         





class NumGuesserGame(Score):  # get x amount of guesses, with one player choosing to guess
    
    def __init__(self,player1,player2):
        super().__init__(player1,player2)
        while True:
                player1_count=0 
                player2_count=0
                number_range= int(input('Player 1, Enter the largest number in your guessing range. You each have 10 chances to guess the number correctly. '))
                answer = random.randint(1,number_range)  # inputs4
                
                number_range2= int(input('Player 2, Enter the largest number in your guessing range. You each have 10 chances to guess the number correctly. '))
                answer2 = random.randint(1,number_range2)  # inputs4   
                x=0
                for x in range(1,12):
                        player1_guess = int(input("\n Player 1, Take a guess. " ))
                        x+=1
                        if player1_guess>answer: 
                            print("Whoops, you missed it. Your're too high.")
                            player1_count+=1
                            print('You have ', 10 - player1_count, ' guesses left.\n')
                        
                        elif player1_guess<answer: 
                            print("\n Your're too low, try guessing higher")
                            player1_count+=1
                            print('You have ', 10 - player1_count, ' guesses left.\n')
                        elif player1_guess == answer: 
                            print('Congrats you got it! The correct number was ', answer,'.')
                            break 
                        
                        if player1_count==10: 
                            print('Sorry, you ran out of guesses. The correct number was,',answer,'.')
                            break
                    
            
                
                
                y=0
                for y in range(1,12):
                        player2_guess = int(input("\n Player 2, Take a guess. " ))
                        y+=1
                        if player2_guess>answer2: 
                                print("Whoops, you missed it. Your're too high.")
                                player2_count+=1
                                print('You have ', 10 - player2_count, ' guesses left.\n')
                            
                        elif player2_guess<answer2: 
                                print("\n Your're too low, try guessing higher")
                                player2_count+=1
                                print('You have ', 10 - player2_count, ' guesses left.\n')
                            
                        elif player2_guess == answer2: 
                                print('Congrats you got it! The correct number was ', answer2,'.')
                                break 

                        if player2_count==10: 
                                print('Sorry, you ran out of guesses. The correct number was,',answer2,'.')
                                break
                Continue = input('Play againz?(y/n):')    # unit test 
                if Continue == 'y': 
                 continue 
                else:
                    break
            
            
            


            
            

                
            
            



           
        
    








class Pig(Score): # pig 
     def __init__(self,player1,player2):
        super().__init__(player1,player2)
        p1_score=0   # insert a while true here 
        p2_score=0
        p1_turn=True
        p2_turn=False
        hold1=False
        hold2=False
        print('\nThe object of Pig is to be the first player to earn 100 points. You achieve this by rolling the dice and adding which number you roll to your overall score. Players are permitted to roll as many times as they’d like during their turn, but beware of rolling a 1! Doing so will cost you all the points you’ve collected during your turn\n')
        while p1_score<=10 or p2_score<=10:
            if hold1 and hold2:
                break;
            else:
                if p1_turn: 
                    if p1_score<10:
                        roll_1= input('Player 1, do you want to roll?(y/n) ')
                        if roll_1=='y':
                            dice1=random.randint(1,6)
                            

                            if dice1==1:
                                    dummy=p1_score
                                    print('Sorry, player 1 rolled a', dice1,' you lost all your points this turn')
                                    print('Your score this turn is', dummy,'\n')
                                    p2_turn=True
                                    p1_turn=False
                                    
                                    
                            elif dice1!=1:
                                
                                    print('Player 1 rolled a ',dice1)
                                    
                                    p1_score=p1_score + dice1
                                    dummy=p1_score
                                    if p1_score>=10:
                                        print('Player one your score is: ',p1_score)
                                        break;
                                    else:print('Player 1, score is', p1_score,'\n')
                                    terminate_turn=input('Do you want to hold?(y/n)')
                                    if terminate_turn=='n':
                                        p2_turn=False
                                        p1_turn=True
                                    else: 
                                        p2_turn=True
                                        p1_turn=False
                                        hold1=True
                                

                                    
                        
                        
                        elif roll_1=='n':   
                            print('Your score is: ', p1_score,)
                            p1_turn=False  
                            p2_turn=True
                            hold1=True
            
                    
                    else:
                        break


                
                
                
                
                elif p2_turn: 
                    if p2_score<10:
                        roll_2= input('Player 2, do you want to roll?(y/n) ')
                        if roll_2=='y':
                            dice2=random.randint(1,6)
                            

                            if dice2==1:
                                    print('Sorry, player2 rolled a', dice2,' you lost all your points this turn\n')
                                    print('Your score is', p2_score)
                                    p2_turn=False
                                    p1_turn=True
                                
                                    
                            elif dice2!=1:
                                
                                    print('Player 2 rolled a ',dice2)
                                    
                                    p2_score=p2_score + dice2
                                    if p2_score>=10:
                                        print('Player 2, your score is: ',p2_score)
                                        break;
                                    else:print('Player 2, your score is', p2_score,'\n')
                                    terminate_turn=input('Do you want to hold?(y/n)')
                                    if terminate_turn=='n':
                                        p2_turn=True
                                        p1_turn=False
                                    else: 
                                        p2_turn=False
                                        p1_turn=True
                                        hold2=True

                                    
                        
                        
                        elif roll_1=='n':   
                            print('Your score is: ', p1_score,)
                            p1_turn=False  
                            p2_turn=True       
                            hold2=True

                    else:
                        break




        if p1_score>p2_score: 
            print('Player 1 score is:',p1_score,'and Player 2 score is:',p2_score)  # send to score here 
            print('player 1 wins with a score of',p2_score)
        elif p1_score<p2_score:         
            print('Player 2 score is:',p2_score,'and Player 1 score is:',p1_score)
            print('player 2 wins with a score of: ',p2_score)
                
            
                            
                            



