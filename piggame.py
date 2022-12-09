import random

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
                    dice1=random.randint(1,3)  # generates dice roll
                    

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
    print('Player 1 score is:',p1_score,'and Player 2 score is:',p2_score)  # send to score here 
    print('player 1 wins with a score of',p2_score)
elif p1_score<p2_score:         
    print('Player 2 score is:',p2_score,'and Player 1 score is:',p1_score)
    print('player 2 wins with a score of: ',p2_score)
        
    
                    
                    