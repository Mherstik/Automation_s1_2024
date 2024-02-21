#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:03:53 2024

@author: marcus
"""

### Homework
# Write the dice roller so it asks 
# how many sides to roll, 
# how many of each dice type to roll
# and continue asking until they stop
# e.g. roll 2 x 10 sided dice, 4 x 6 sided, 1 x 20 sided


'''
Create a Python program that simulates rolling a dice (e.g., a standard six-sided die).
The program should generate a random number between 1 and 6 to mimic the roll of a die.

Ask the user how many sides they want on the dice
'''

def roll_dice():
    pass
    # for dice in dice_roll:
            

user_dice = []
user_rolls = []

while True:
    sides = input("Press 'X' to exit\nHow many sides for a dice to roll: ")
    if sides.lower() == 'x':
        break
    else:
        try:
            sides = int(sides)
            while True:
                rolls = input(f"How many rolls of {sides} sided dice to roll: ")
                if rolls.lower() == 'x':
                    break
                else:
                    try:
                        rolls = int(rolls)
                        user_rolls.append(rolls)
                        user_dice.append(sides)
                        break
                    except:
                        print("invalid number. Please give number of rolls again")           
        except:
            print("Invalid number. Try again")
    
