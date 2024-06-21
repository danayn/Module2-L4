#Assignment: Python Loop Statements
'''
1. The Range Riddle

Objective:
The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. 
You will correct a code snippet, simulate moods for different days, and create a countdown timer.

Task 1: Your Mood Today
Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", 
"Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a 
mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

'''
import random 

moods = ["Happy", "Sad", "Energetic", "Calm"]
dayw = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
x = ""
y = ""
for i in range(7):
    y = dayw[i]
    x = random.choice(moods)
    print("'On "+y+", you were feeling "+x+".'")
