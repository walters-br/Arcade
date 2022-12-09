import random as rand 
import time
print('Categories')


 
alphabet= "abcdefghijklmnopqrstuvwxyz" # s
input('Please enter a category for both players to guess in to ')
print('You can enter any item into the category that beings with:',rand.choice(alphabet),"\n") # selects random number from the alphabet string

player1_set=set() #empty set for each category per player
player2_set=set()


time.sleep(1)
print("Player 2, you have 30 seconds to enter into the first category ")   # prompts player 1 to enter into the category
time.sleep(1)
print("Start!\n")


timeout = time.time() + 10   # 30 seconds minutes from now
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


timeout2 = time.time() + 30   # 30 seconds from now
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

elif len(player1_set) < len(player2_set):
     print("Player 2 has more entreies, Player 2 wins") 
else: 
    print('There was a tie')




