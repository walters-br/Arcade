#21 questions 

starter=input('which player wants to go first?(1/2)')

if starter=='1':
    answer_string=input('Player 1, please enter your answer: ')
  
    
    for i in range(20):
        question_string=input('Player 2, ask your question:')

        
        if question_string==answer_string:
            print('You got it! The answer was',answer_string)
        elif question_string!=answer_string:
            print('Wrong Guess: Try again')
            
        

else:
