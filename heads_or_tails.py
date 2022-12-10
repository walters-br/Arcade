
import random 
p1_score=0
p2_score=0
while True: 
    answer = random.randint(1,2)  # gets a random num netween 1 and 2 that will represent the sides of a coin
    player1_guess = input(" Player 1, State your guess (H or T): ")  # aks players to choose what the coin will be 
    player2_guess = input(" Player 2, State your guess (H or T): ")
    
    
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
    if answer==1:
        coin="Heads"

    if player1_guess == answer:
            print('Player 1 guessed right, the answer was: ', coin)
            p1_score+=1
    else: 
            print('Player 2 guessed right, the answer was: ', coin)
            p2_score+=1

    Continue = input('Play againz?(y/n):')    # unit test 
    if Continue == 'y': 
        continue 
    else:
        break

