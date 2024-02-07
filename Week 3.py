#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:13:55 2024

@author: marcus
"""

## Grade check code!

## Fail          0 - 49
#   Pass        50 - 65
#   Credit      65 - 75
#   Distinction 75 - 85
#   HD          85 +

# Put in a score and get their grade
# check it's a number.
# Say their name and their grade.
# Input: Name, Score
# Output: Name, Grade
# Description: 
# Get users grade from score

# Get name

name = input("Give me your name please: ")


# # Read score between 0 -100
while True:
    score = input("Give me your score: ")
    if score.isdigit():
        score = int(score)
        #if score >= 0 and score <= 100:
        if score in range(0,101):
            break
        else:
            print("Not a valid number")
    else:
        print("Not a valid number")

# #score = input("Give me your score: ")
# try:
#     score = float(input("Enter the student's score (0-100): "))
#     if score < 0 or score > 100:
#         print("Invalid score. The score must be between 0 and 100.")
# except ValueError:
#     print("Invalid input. Please enter a numeric value for the score.")



if score < 50:
    print(name, "Failed")
# if score between 50 and 64
elif score >=50 and score <= 64:
    print(name, "passed")
# if score between 65 and 74
elif score >=65 and score <= 74:
	print("Credit")
# if score between 75 and 84
elif score >=75 and score <= 84:
 	print("Distinction")
# if score above 85
else: 
    print("HD")
# 	HD
	
