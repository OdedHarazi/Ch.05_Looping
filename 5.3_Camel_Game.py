import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''


print("Instructions:")
done = False
dead = False
thirst = 0
miles = 0
camel = 0
water = 3
natives = -20

while not done:

        print("A) Drink Water")
        print("B) Keep Moving Slowly")
        print("C) Full Speed Ahead")
        print("D) Stop for the night")
        print("E) Status Check")
        print("Q) Quit")
        if thirst >= 6:
            print("You died of thirst!")
            done = True
            quit()
        if thirst >= 4 and thirst < 6:
            print("You are thirsty! \n")
        if camel >= 5 and camel < 8:
            print ("Your camel is very tired!")
        if camel >=8:
            print ("Your camel has died. You are a terrible person.")
            done = True
            quit() #Added Quit due to an error that continued the game after death
        if natives >= miles:
            print("The natives caught up to you!")
            done = True
        if miles-natives <= 15:
            print("The natives are close!")
        if miles >= 200:
            print("You've won")
            print("Congratulations!")
            input("Any words of advice for upcoming gamers:")
            print("OMG You are so RIGHT!")
            done = True
        else:
            choice = input("Select a Character:")
            # To Quit
            if choice.lower() == "q":
                done = True
                print("Thanks for Playing!")
            # Status Check
            elif choice.lower() == "e":
                print("\n Miles Traveled:" ,miles)
                print("Drinks in Canteen:", water)
                print("The Natives are", miles - natives, "miles behind you!")
            #     Stopping for the night code:
            elif choice.lower() == "d":
                print("\n The Camel is Happy With Your Decision")
                print("*Camel Licks*")
                camel = 0
                nativesdistance = random.randrange(7,15)
                natives += nativesdistance
            #  Full Speed Ahead
            elif choice.lower() == "c":
                milestraveled = random.randrange(10,20)
                nativesdistance = random.randrange(7,15)
                tired = random.randrange(1,4)
                thirst+=1
                camel += tired
                miles += milestraveled
                print("\n Full Speed Ahead!")
                print("You traveled",milestraveled,"miles!")
                oasis = random.randrange(1,21)
                if oasis == 1:
                    print("You've found an oasis!")
                    camel = 0
                    thirst = 0
                    water = 3
            #  Moving Slowly
            elif choice.lower() == "b":
                milestraveled = random.randrange(5,13)
                nativesdistance = random.randrange(7,15)
                thirst += 1
                camel += 1
                miles += milestraveled
                print("\n You traveled",milestraveled,"miles!")
                oasis = random.randrange(1, 21)
                if oasis == 1:
                    print("You've found an oasis!")
                    camel = 0
                    thirst = 0
                    water = 3
            #   Drinking Water
            elif choice.lower() == "a" and water > 0:
                water -= 1
                thirst = 0
                print("\nYou are no longer thirsty!")
