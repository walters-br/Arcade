# hangman 
intialize=True
player1_win=0
while intialize: 
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
            break   # add a do you want to continue here 
        elif num_of_guesses==6 :
            print('Sorry the word was',answer_string )
            break


    
    
    
    
    
    
    
    else: 
        answer_string2=input('Player 2, enter the word if your choice')

    
    