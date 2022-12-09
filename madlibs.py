


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
else: 
    print('Player 2 wins')



