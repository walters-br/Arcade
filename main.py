import random
import time
class Score(): # keeps traack of score, every class will inherit it's score keep properties   
    def __init__(self,score1,score2) -> None:
      
       self.score2  =score2
       self.score1 = score1
    def add_score1(self, num):# each class needs a way to store score and return it 
        self.score1 = self.score1 + num 
    def add_score2(self,num):
        self.score2 = self.score2 + num
    def __str__(self) -> str:
         print(f"Overall Player 2 has a score of: ",{self.score2},"\n and Player 1 has a score of: ",{self.score1}) #print statement for scrore across all the games 
# Each instance of any below game assumes 2 players 

class RPS(Score): # rock paper scissors
    def __init__(self,score1,score2):
        super().__init__(score1,score2) 
    def start(self):
     while True:
        player1input= input("Player One Choose Rock,Paper,or Scissors\n")
        player2input = input("Player Two Choose Rock,Paper,or Scissors\n")
        if player1input == player2input: 
            print(f"It's a draw, both players selected",{player2input})
    
        elif player1input == "Rock": 
                if player2input=="Scissors":
                    print("Player 1 wins, Rock beats Scissors")   # add class specific object here 
                    self.add_score1(1)
                else: 
                    print("Player 2 wins Paper Covers Rock")
                    self.add_score2(1)
        
        elif player1input == "Scissors":
                
                if player2input == "Rock":
                    print("Player 2 wins, Rock beats Scissors")   # add class specific object here 
                    self.add_score2(1)
                else: 
                    print("Player 1 wins, Scissors cuts paper")
                    self.add_score1(1)

        
        elif player1input == "Paper": 
            if player2input =="Rock":
                    print("Player 1 wins, Paper beats Rock")   # add class specific object here 
                    self.add_score1(1)
            else: 
                    print("Plater 2 wins, Scissors beats Paper")
                    self.add_score2(1)

    
       
        Continue = input('Play againz?(y/n):')    # unit test 
        if Continue == 'n': 
            break 
       
        else: 
            continue 



class madlibs(Score): #madlibs game, gives player 1 or 2 a score if the other finds it funny
    def __init__(self,score1,score2):
        super().__init__(score1,score2) # gets player names from Score patent class
    def start(self):
        while True:
            adj1= input('PLayer 1 Enter an Adjective: ')
            adj2= input('Player 1, Enter another Adjective: ')
            noun1=input('Player 1 Enter a noun: ')
            noun2 = input('Player 1 Enter another noun: ')
            game=  input('Player 1 Enter a game: ')

            pluralnoun1=input('Player 1Enter a plural noun:')
            verb_ending_w1=input('Player 1 Enter a verb ending with ing\": ')
            verb_ending_w2=input('Player 1 Enter another verb ending with ing\": ')


            madlib = f"\n A vacation is when you take a trip to some {adj1} place with your {adj2} family. \
            Usually you go to some place that is near a/an {noun1} or up a/an a {noun2}. A good vacation place is one where you can ride or play\
            {game} or go hunting for {pluralnoun1}. I like to spend my time {verb_ending_w1} or {verb_ending_w2}" # inserts the words above into the madlib  string based on user input 

            print("Player 1's madlib was: \n \n \n ",madlib)  # prints player 1 madlib






            adj3= input('Enter an Adjective: ')
            adj4= input('Enter another Adjective: ')
            noun3=input('Enter a noun: ')
            noun4 = input('Enter another noun: ')   #prompts player 2 to enter the words to complete the amdlib string
            game2=  input('Enter a game: ')

            pluralnoun3=input('Enter a plural noun:')
            verb_ending_w3=input('Enter a verb ending with ing\": ')
            verb_ending_w4=input('Enter another verb ending with ing\": ')


            madlib2= f"\n A vacation is when you take a trip to some {adj3} place with your {adj4} family. \
            Usually you go to some place that is near a/an {noun3} or up a/an a {noun4}. A good vacation place is one where you can ride or play\
            {game2} or go hunting for {pluralnoun3}. I like to spend my time {verb_ending_w3} or {verb_ending_w4}"    # inserts the words above into the madlib  string based on user input

            print("Player 2's madlib was: \n \n \n ",madlib2)  # prints player 1 madlib

            playerwinner=input("Which player had the more entertaining madlib?(1/2)")

            if playerwinner==1:
                print('Player 1 wins ')
                self.add_score1(1)   # adds score to player 1 
            else: 
                print('Player 2 wins')
                self.add_score2(1)  # adds score to player 2 
            
            Continue = input('Play againz?(y/n):')    # unit test 
            if Continue == 'n': 
                break 
        
            else: 
                continue 


class Hangman(Score):  # hangman game 
    def __init__(self,score1,score2):
        super().__init__(score1,score2) 
    def start(self):
        
        while True: 
          start = int(input('Which player wants to create a word (1 or 2)\n'))
          
          if start==1: 
                answer_string = input('Player 1 , enter a word of your choice. Make sure Player 2 is looking away. ')
                answer_string= answer_string.upper()
                num_of_guesses = 0
                attempts=[]
                word_display= "_" * len(answer_string)
                Win = 0
                print('Player 2, you have 6 tries to guess the word. Enter one letter at a time ')
            
                while num_of_guesses < 8 :
                    guess=input('Player 2, please guess a letter: ').upper() # turns all guesses into uppercase form
        
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
                        print('You guessed the word, the word was', answer_string)
                        self.add_score2(1)   # adds score to player 1 
                        break   # add a do you want to continue here 
                    elif num_of_guesses==6 :
                         print('Sorry the word was',answer_string )
                         break


    
    
    
    
    
        
          else: 
                answer_string2 = input('Player 1 , enter a word of your choice. Make sure Player 2 is looking away. ')
                answer_string2= answer_string2.upper()
                num_of_guesses = 0
                attempts=[]
                word_display= "_" * len(answer_string2)
                Win = 0
                print('Player 1, you have 6 tries to guess the word. Enter one letter at a time ')
            
                while num_of_guesses < 8 :
                    guess=input('Player 1, please guess a letter: ').upper() # turns all guesses into uppercase form
        
                    if len(guess)==1 and guess.isalpha(): # if player enters a letter and is a letter
            
            
            
                        if guess not in answer_string2:
                            print('Sorry,', guess,'is not in the word')
                            num_of_guesses +=1
                            print('You have ',6-num_of_guesses,' left.')
                            attempts.append(guess) # throws the guess into a list of previous guesses
                        else:
                            print('Good choice' , guess, ' is in the word')
                            attempts.append(guess)
                            correct_attempts_display=list(word_display)
                            indices = [x for x, letter in enumerate(answer_string2) if letter==guess]
                            for index in indices: 
                                correct_attempts_display[index]=guess
                                word_display=''.join(correct_attempts_display)
                            if '_' not in word_display: 
                                Win=1
                    else:
                        print('Not a valid guess')
        
                    if Win==1:
                        print('You guessed the word, the word was', answer_string)
                        self.add_score1(1)   # adds score to player 1 
                        break   # add a do you want to continue here 
                    elif num_of_guesses==6 :
                         print('Sorry the word was',answer_string )
                         break
            
        
          Continue = input('Play againz?(y/n):')    # unit test 
          if Continue == 'n': 
                    break 
       
          else: 
                    continue 
         

    
    
    
    
    

class Categories(Score): # twenty one questions game 
     def __init__(self,score1,score2):
        super().__init__(score1,score2)
        
     def start(self):
        while True: 
          
            print('Categories')
            alphabet= "abcdefghijklmnopqrstuvwxyz" # string with alphabet 
            input('Please enter a category for both players to guess in to ')
            print('You can enter any item into the category that beings with:',random.choice(alphabet),"\n") # selects random number from the alphabet string

            player1_set=set() #empty set for each category per player
            player2_set=set()


            time.sleep(1)
            print("Player 2, you have 20 seconds to enter into the first category ")   # prompts player 1 to enter into the category
            time.sleep(1)  # sets a delay of 1 second before calling the next line
            print("Start!\n")


            timeout = time.time() + 20   # 20 seconds minutes from now
            while True:
                user_input=input('Please enter a word:') 
                player1_set.add(user_input)     # appends user input into list  
                if time.time() > timeout:  # allows to add to the cateogry for up to 30 seconds
                    print('Time Up')
                    break

            print(player1_set,"\n")

            time.sleep(1)
            print("Player 2, you have 30 seconds to enter into the first category ")   # prompts player 1 to enter into the category
            time.sleep(1)
            print("Start!\n")


            timeout2 = time.time() + 20   # 20 seconds from now
            while True:
                user_input=input('Please enter a word:') 
                player2_set.add(user_input)     # appends user input into list  
                if time.time() > timeout2:  # allows to add to the cateogry for up to 30 seconds
                    print('Time Up \n')
                    break

            print(player2_set,"\n")

            time.sleep(2)
            if len(player1_set) > len(player2_set):
                print("Player 1 had more entries, Player 1 wins") 
                self.add_score1(1)   # adds score to player 1 

            elif len(player1_set) < len(player2_set):
                print("Player 2 has more entreies, Player 2 wins") 
                self.add_score2(1)   # adds score to player 2
            else: 
                print('There was a tie')

            Continue = input('Play again?(y/n):')
            if Continue == 'n': 
                  break 
            else: 
                continue 
             
                    
          



            
          








class HeadsOrTails(Score):  # each player bets on heads or tail 
   
     def __init__(self,score1,score2):
        super().__init__(score1,score2)
        
     def start(self):  
        
        while True: 
          answer = random.randint(1,2)  # gets a random num netween 1 and 2 that will represent the sides of a coin
          player1_guess = input(" Plater 1, State your guess H or T")  # aks players to choose what the coin will be 
          player2_guess = input(" Plater 1, State your guess H or T")
          
          
          if player1_guess == "H":  #
                player1_guess=1 
          if player2_guess == "H": 
                player2_guess=1
         

          if player1_guess == "T": 
                player1_guess=2 
          if player2_guess == "T": 
                player2_guess=2

          if answer==2:
            coin="Tails"
          if answer==1:  # determines coin based on the answer number 
              coin="Heads"
         
          if player1_guess == answer:
                 print('Player 1 guessed right, the answer was: ', coin)  # determines the winner and displays the coin
                 self.add_score1(1)  # adds 1 point to player 1 score in the "Score" class 
          else: 
                 print('Player 2 guessed right, the answer was: ', coin)
                 self.add_score2(1)
        
          Continue = input('Play againz?(y/n):')    # unit test 
          if Continue == 'y': 
             continue 
          else:
            break




            
          
            
         





class NumGuesserGame(Score):  # get x amount of guesses, with one player choosing to guess
    
    def __init__(self,score1,score2):
        super().__init__(score1,score2)

    def start(self):
        while True:
                player1_count=0 
                player2_count=0
                number_range= int(input('Player 1, Enter the largest number in your guessing range. You each have 10 chances to guess the number correctly. '))   #asks both users to specify the range that the number could be within
                answer = random.randint(1,number_range)  # gets the number from the specified range
                
                number_range2= int(input('Player 2, Enter the largest number in your guessing range. You each have 10 chances to guess the number correctly. '))
                answer2 = random.randint(1,number_range2)   # gets the number from the specified range
                
                x=0
                for x in range(1,12):  # each game has 10 guesses to get the correct NUMBER, having a range to 12 ensures the game never terminates before any unused guesses
                        player1_guess = int(input("\n Player 1, Take a guess. " )) # asks the user to guess 
                        x+=1 
                        if player1_guess>answer: #informs user when the guess is too high
                            print("Whoops, you missed it. Your're too high.") 
                            player1_count+=1 
                            print('You have ', 10 - player1_count, ' guesses left.\n')    # prints remaining guesses left 
                        
                        elif player1_guess<answer:  #informs user when the guess is too low
                            print("\n Your're too low, try guessing higher")
                            player1_count+=1
                            print('You have ', 10 - player1_count, ' guesses left.\n')
                        elif player1_guess == answer: 
                            print('Congrats you got it! The correct number was ', answer,'.')   # make sure to add score to score class 
                            self.add_score1(1)  # adds to player 1 score 
                            break 
                        
                        if player1_count==10:  # statement for when the user runs out of guesses
                            print('Sorry, you ran out of guesses. The correct number was,',answer,'.') # prints the correct answer 
                            break                               # breaks while loop to continue into player 2's turn
                    
            
                
                
                y=0
                for y in range(1,12): # each game has 10 guesses to get the correct NUMBER
                        player2_guess = int(input("\n Player 2, Take a guess. " ))
                        y+=1
                        if player2_guess>answer2:                                                                   #Player 2 game is written the same as Player 1. 
                                print("Whoops, you missed it. Your're too high.")
                                player2_count+=1
                                print('You have ', 10 - player2_count, ' guesses left.\n')
                            
                        elif player2_guess<answer2: 
                                print("\n Your're too low, try guessing higher")
                                player2_count+=1
                                print('You have ', 10 - player2_count, ' guesses left.\n')
                            
                        elif player2_guess == answer2: 
                                print('Congrats you got it! The correct number was ', answer2,'.')
                                self.add_score2(1)
                                break 

                        if player2_count==10: 
                                print('Sorry, you ran out of guesses. The correct number was,',answer2,'.')
                                break
                
                Continue = input('Play againz?(y/n):')    # prompts users to play the game again or break and terminate 
                if Continue == 'y': 
                 continue 
                else:
                    break
            
            
            


            
            

                
            
            



           
        
    








class Pig(Score): # pig 
     def __init__(self,score1,score2):
        super().__init__(score1,score2)
         
     def start(self):
        p1_score=0   # variable declarations 
        p2_score=0
        p1_turn=True  # flags to determine which palyer is going first or second. Player 1 alawyas goes first 
        p2_turn=False  
        hold1=False
        hold2=False
        dummy=0
        dummy2=0
        print('\nThe object of Pig is to be the first player to earn 50 points. You achieve this by rolling the dice and adding which number you roll to your overall score. Players are permitted to roll as many times as they’d like during their turn, but beware of rolling a 1! Doing so will cost you all the points you’ve collected during your turn\n') 
                    # prints instructions 
        while p1_score<=50 or p2_score<=50: # while both scores are less than 50
            if hold1 and hold2:
                 break;
            else:
                if p1_turn: 
                    if p1_score<50: # another condition to ensure both scores are less than 50
                        roll_1= input('Player 1, do you want to roll?(y/n) ') # prompts the user to hold or roll
                        if roll_1=='y':
                            dice1=random.randint(1,6)  # generates dice roll
                        

                            if dice1==1:   # when a dice roll is "1" the player forfeights points earned
                                    # dummy keeps track of the score at the time "1" is rolled 
                                    print('Sorry, player 1 rolled a', dice1,' you lost all your points this turn')
                                    print('Your score is now', dummy,'\n')  #dummy becomes 
                                    p1_score=dummy
                                    p2_turn=True
                                    p1_turn=False
                                    
                            
                            elif dice1!=1:
                                
                                    print('Player 1 rolled a ',dice1)
                                    
                                    p1_score=p1_score + dice1
                                    if p1_score>=50:
                                        print('Player one your score is: ',p1_score)
                                        break;
                                    else:print('Player 1, score is', p1_score,'\n')
                                    terminate_turn=input('Do you want to hold?(y/n)')
                                    if terminate_turn=='n':
                                        p2_turn=False
                                        p1_turn=True
                                    else: 
                                        dummy=p1_score
                                        p2_turn=True
                                        p1_turn=False
                                        hold1=True
                        

                            
                
                    
                    elif roll_1=='n':   
                        print('Your score is: ', p1_score,)
                        dummy=p1_score
                        p1_turn=False  
                        p2_turn=True
                        hold1=True
    
            
                    else:
                        break


        
        
        
        
                elif p2_turn:  # statement when it's player 2's turn
                    if p2_score<50:
                        roll_2= input('Player 2, do you want to roll?(y/n) ')
                        if roll_2=='y':
                            dice2=random.randint(1,3)
                            

                            if dice2==1:
                                    print('Sorry, Player 2 rolled a', dice2,' you lost all your points this turn\n')
                                    print('Your score is now ', dummy2)
                                    p1_score=dummy2
                                    p2_turn=False
                                    p1_turn=True
                                
                                    
                            elif dice2!=1:
                                
                                    print('Player 2 rolled a ',dice2)
                                    
                                    p2_score=p2_score + dice2
                                    if p2_score>=50:
                                        print('Player 2, your score is: ',p2_score)
                                        break;
                                    else:print('Player 2, your score is', p2_score,'\n')
                                    terminate_turn=input('Do you want to hold?(y/n)')
                                    if terminate_turn=='n':
                                        p2_turn=True
                                        p1_turn=False
                                    else: 
                                        p2_turn=False
                                        dummy2=p1_score
                                        end_game= input('Player 1 do you want hold and end the game?(y/n)')
                                        if end_game=='y':
                                            hold2=True
                                        else:
                                            p1_turn=True

                            
                
                
                        elif roll_1=='n':   
                            print('Your score is: ', p1_score,)
                            dummy2=p2_score
                            p1_turn=False  
                            p2_turn=True       
                            hold2=True

                    else:
                        break
  
        if p1_score>p2_score: 
                    print('Player 1 score is:',p1_score,'and Player 2 score is:',p2_score)  
                    print('player 1 wins with a score of',p2_score)
                    self.add_score1(1) # send to score here 
        elif p1_score<p2_score:         
                    print('Player 2 score is:',p2_score,'and Player 1 score is:',p1_score)  # displays the score the winner won by 
                    print('player 2 wins with a score of: ',p2_score)
                    self.add_score2(1) 
        
    
                    



        
                    
                            
                            



