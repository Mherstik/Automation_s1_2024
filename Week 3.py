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


# Read score between 0 -100
while True:
    score = input("Give me your score: ")
    if score.isdigit():
        score = int(score)
        if score >= 0 and score <= 100:
            break
        else:
            print("Not a valid number")
    else:
        print("Not a valid number")


# if score < 50
# 	Fail
# if score between 50 and 64
# 	Pass
# if score between 65 and 74
# 	Credit
# if score between 75 and 84
# 	Distinction
# if score above 85
# 	HD
	
