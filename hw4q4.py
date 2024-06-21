#Assignment: Python Loop Statements
'''
4. Python's Random Game Night

Objective:
The aim of this assignment is to explore the random package in Python and understand 
how it can be used with loops to introduce randomness into your programs.

Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. 
Use random.choice() to select the item and take the user's guess via input. 
Provide feedback on whether they guessed correctly or not.

'''
import random

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = random.choice(items)
print("This is a Random Choice Game")
guess = int(input("Guess the randomly chosen number by entering a number (1 - 10) and enter 0 if you want to exit: "))
if(guess == x):
    print("The number you have guessed is correct. Well done!")
elif(guess == 0):
    print("You have exited the game. Thank You for playing!")
else:
    print("You have guessed incorrectly. Try again in next game.")

