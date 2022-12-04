
import random
player1_dice_score=0
player2_dice_score=0
while True: 
            print('The object of Pig is to be the first player to earn 100 points. You achieve this by rolling the dice and adding which number you roll to your overall score. Players are permitted to roll as many times as they’d like during their turn, but beware of rolling a 1! Doing so will cost you all the points you’ve collected during your turn')
            player1_guess=(input('Player 1, do you wish to roll? (y/n)'))
            
            if player1_guess=='y': 
                while player1_guess =='y':
                    dice1= random.randint(1,6)
                    if dice1==1:
                        print('sorry, you rolled a', dice1,'  you lost all your points this turn:')
                        player1_guess=='n'
                        
                    if dice1!=1:
                        print('You rolled a ',dice1)
                        player1_dice_score+=dice1
                        print('Player 1, score is', player1_dice_score)
                        player1_guess=(input('Do you wish to roll again? (y/n)'))
                        
    
            
            elif player1_guess=='n': 
             player2_guess=(input('Player 2, do you wish to roll? (y/n)'))
             if player2_guess=='y':
                    dice2= random.randint(1,6)
                    while player2_guess =='y':
                        if dice2==1:
                            print('sorry, you rolled a 1, you lost all your points this turn:')
                            break;
                        elif dice2!=1:
                             print('You rolled a ',dice2)
                             player2_dice_score+=dice2
                             print('Player 2, score is', player2_dice_score)
                             player2_guess=(input('Do you wish to roll again? (y/n)'))