from random import randrange

#initialize players and choices 
Player_Options=["1","2","3"] #difficulty level
Choices=["rock.","paper.","scissors."]
Bot_Loses=["scissors.","rock.","paper."]
Bot_Wins=["paper.","scissors.","rock."]
Difficulties=Player_Options

def Play(x,y):
	if Bot in range(1,x):
		Win()
	elif Bot in range(x,y):
		Draw()
	else:
		Lose()

def Win():
    Message(Choices, Bot_Loses,"You win!")

def Draw():
    Message(Choices,Choices,"It's A draw!")

def Lose():
    Message(Choices,Bot_Wins,"You lost!")
    
def Message(PlayerChoice,BotChoice,OutcomeMessage):
    print("You choose",PlayerChoice[P1ayer],"Bot choose",BotChoice[P1ayer])
    print(OutcomeMessage)
   
while True:

    #Difficulty level 
    while True:
        Bot=randrange(1,11)
        print("Press 1 for Easy, 2 for Medium, and 3 for Hard ")
        Difficulty=input("Select Difficulty: \n")
        if Difficulty in Difficulties:
            Diff=int(Difficulty)

            #Easy
            if Diff==1:
                print("You Choose Easy!")
                while True:
                    Player=input("\nPick 1 for Rock, 2 for Paper, and 3 for Scissors: \n")
                    if Player in Player_Options:
                        P1ayer=int(Player)-1
                        Play(6,9)
                        break
                    else:
                        continue

            elif Diff==2:
                print("You Choose Medium!")
                while True:
                    Player=input("\nPick 1 for Rock, 2 for Paper, and 3 for Scissors: \n")
                    if Player in Player_Options:
                        P1ayer=int(Player)-1
                        Play(5,7)
                        break
                    else:
                        continue

            else:
                print("You Choose Hard!")
                while True:
                    Player=input("\nPick 1 for Rock, 2 for Paper, and 3 for Scissors: \n")
                    if Player in Player_Options:
                        P1ayer=int(Player)-1
                        Play(4,7)
                        break
                    else:
                        continue                
            break
    
        else:
            continue #Player didn't choose valid difficulty
    
    Replay=input("\nThank you for Playing! \nEnter X to quit, Enter any key to play again. \n")
    if Replay=="x" or Replay=="X":
        break
