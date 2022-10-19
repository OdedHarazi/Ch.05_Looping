import random
  #Sign your name:________________

'''
#  1. Make the following program work.
#    '''

print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
      num = int(input("Enter a Number"))
      total+=num
print("The total is:",total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
print("All Even Numbers 1-100")
for i in range(101):
      if i%2 == 0:
           print(i)



'''
#   3. Write a program that will use a WHILE loop to count from
#      10 down to, and including, 0. Then print the words Blast off! Remember, use
#      a WHILE loop, don't use a FOR loop.
'''
print("THE ROCKET IS TAKING OFF IN")
var=9
print("T-Minus 10!")
while var >= 0:
      print(var)
      var-=1
print("BLAST OFF!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
print("Your Random Integer is:")
for i in range(1):
      num = random.randrange(10)
      print(num)



'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program takes seven numbers and analyzes them")
total = 0
pos = 0
zero = 0
neg = 0
for i in range(7):
      num = int(input("Enter a Number: "))
      if num > 0:
            pos += 1
      elif num < 0:
            neg +=1
      else:
            zero +=1
      total+=num
print("The total is:",total)
print("You entered",pos,"positive numbers")
print("You entered",neg,"negative numbers")
print("You entered zero",zero,"time(s)")




-----------------------------------------------------------------------------------------------------------------------------------------------------------
# IGNORE BELOW:------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# a=0
# for i in range(10):
#       a+=1
#       for j in range (10):
#             a+=1
# for i in range(10):
#       print(i)
# PERSEVERANCE GAME
# done = False
# perseverance = 0
# while not done:
#       quit = input("Do you want to quit? (Type y)")
#       if quit.lower()=="y":
#             done = True
#       else:
#             perseverance+=1
# print("Goodbye! Your perseverance level is " , perseverance)
#
#GUESS THE NUMBER GAME
# for i in range(1):
#       done = False
#       num = random.randrange(100)
#       while not done:
#             guess = input("Guess the number 1-100:")
#             if guess == num:
#                   done = True
#             print("Correct! Good Work!")
#             elif guess > num:
#             guess+=1
#                   print("Too High! Try Again")
#             elif guess < num:
#             guess+=1
#                   print("Too Low! Try Again")
# PRINTING DEATH STAR
# for letter in "Death Star":
#       if letter == " ":
#             break
#       print('Current letter: ',letter)


# import random
#

# total = 0
#
# for i in range(3):
#     x = input("Enter a number: ")
#     total = total + i
# print("The total is:", x)
#


'''            else:
                  perseverance += 1
      print("Goodbye! Your perseverance level is ", perseverance)
'''