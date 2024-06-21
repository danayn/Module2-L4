#Assignment: Python Loop Statements
'''
2. Double Scoop with Nested Loops

Objective:
The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, 
simulate a mood tracker, and generate a multiplication table.

Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and 
the inner loop should iterate over the times of the day. For each time, randomly select a mood from a 
predefined list and print it.

Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" 
"On Wednesday morning you were tired"

'''

import random 

moods = ["Happy", "Sad", "Energetic", "Calm"]
dayw = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
x = ""
y = ""
c = 0
for i in range(7):
    y = dayw[i]
    c = 0
    for p in range(3):
        x = random.choice(moods)
        print("'On "+y+" morning you were feeling "+x+".'")
        c = c + 1
        x = random.choice(moods)
        print("'On "+y+" afternoon you were feeling "+x+".'")
        c = c + 1
        x = random.choice(moods)
        print("'On "+y+" evening you were feeling "+x+".'")
        c = c + 1
        if(c >= 3):
            break
   
   

   