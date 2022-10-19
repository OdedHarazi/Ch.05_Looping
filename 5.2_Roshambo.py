'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random
print("")
print("Welcome to Rock, Paper, Scissors. Select any number from the list below to play a game against the computer.")
print("OR Press \"3\" to Quit")

done = False

Losses = 0
Wins = 0
Ties = 0

while not done:
    for i in range(1):
        num = random.randrange(3)

    print("0) Rock")
    print("1) Paper")
    print("2) Scissors")


    game = int(input("Choose an Number:"))
    # if game >= '0':
    #     print("yup")
    # exit()
    if game == 3:
            done = True
            print("")
            print("")
            print("Goodbye!")

    else:
        if game == num:
            print("It's a Tie")
            Ties += 1
            if num == 0:
                print("We both chose Rock!")
                print("")
            elif num == 1:
                print("We both chose Paper!")
                print("")
            else:
                print("We both chose Scissors!")
                print("")
        elif game == num+1 and num<3 or game == 0 and num == 2:
            print("You Won!")
            Wins += 1
            if num == 0:
                print("You chose Paper! The computer chose Rock!")
                print("")
            elif num == 1:
                print("You chose Scissors! The computer chose Paper!")
                print("")
            else:
                print("You chose Rock! The computer chose Scissors!")
                print("")

        elif game == 2 and num == 0 or game == 1 and num == 2 or game == 0 and num == 1:
            print("You Lost!")
            Losses += 1
            if num == 0:
                print("You chose Scissors! The computer chose Rock!")
                print("")
            elif num == 1:
                print("You chose Rock! The computer chose Paper!")
                print("")
            else:
                print("You chose Paper! The Computer chose Scissors!")
                print("")
        else:
            print("Not an Option...Try Again!")
            print("")

print("Wins:", Wins)
print("Losses:", Losses)
print("Ties:",Ties)

