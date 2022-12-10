from main import Score 
from main import RPS
from main import madlibs
from main import Hangman
from main import Categories
from main import HeadsOrTails
from main import NumGuesserGame
from main import  Pig

A=Score(0,0)

print("\nWelcome to the Mini Arcade. Please select from the Menu below to begin \n")
while True:
    print("\nPress 1 to play Rock Paper Scissors")
    print("Press 2 to play a Madlibs Game: ")
    print("Press 3 to play Hangman: ")
    print("Press 4 to play Categories: ")
    print("Press 5 to play a CoinFlip Guesser: ")
    print("Press 6 to play a Number Guesser: ")
    print("Press 7 to play PIG: ")
    print("Press 8 to check the Score both players have earned")
    Menu=input("Press 9 to Exit: \n")

    if Menu=='1':
        print('\n')
        One = RPS(0,0)
        One.start()
    elif Menu=='2':
        print('\n')
        Two = madlibs(0,0)
        Two.start()
    elif Menu=='3':
        print('\n ')
        Three = Hangman(0,0)
        Three.start()
    elif Menu=='4':
        print('\n')
        Four = Categories(0,0)
        Four.start
    elif Menu=='5':
        print('\n')
        Five = HeadsOrTails(0,0)
        Five.start()
    elif Menu=='6':
        print('\n')
        Six = NumGuesserGame(0,0)
        Six.start()
    elif Menu=='7':
        print('\n')
        Seven=Pig(0,0) 
        Seven.start()
    elif Menu=='8':
            while True:
                print("\n")
                print("Press 1 to view Rock Paper Scissors Score: ")
                print("Press 2 to View Madlibs Score: ")
                print("Press 3 to view Hangman Score: ")
                print("Press 4 to view the Categories Score: ")
                print("Press 5 to view the CoinFlip Guesser Score: ")
                print("Press 6 to view the Number Guesser Score: ")
                print("Press 7 to view PIG Score : ")
                Score_Menu=input("Press 8 to Exit: \n")

                if Score_Menu=='1':
                        One.__str__()
                elif Score_Menu=='2':
                        print('good test. ')
                        Two.__str__()
                elif Score_Menu=='3':
                        Three.__str__()
                elif Score_Menu=='4':
                        Four.__str__()
                elif Score_Menu=='5':
                        Five.__str__()
                elif Score_Menu=='6':
                        Six.__str__()
                elif Score_Menu=='7':
                        Seven.__str__()
                elif Score_Menu=='8':
                        break
                else:
                    Score_Menu=input('Invalid Input. Try Again. ')
   
    elif Menu=='9':
            print('Thank you for Playing. ')
            break
    else:
        Menu=input('Invalid Input. Try Again. ') 
    

