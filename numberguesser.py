from random import random 
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