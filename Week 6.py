#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:03:53 2024

@author: marcus
"""

def calc_average(*args):
    # calculate the total
    total = sum(args)
    avg = total / len(args)
    return round(avg, 2)

print(calc_average(65,57,89,48))

def calculate_grade(average):
    pass


def display_results(name, average, letter_grade):
    pass

# Student: Alice
# Average Grade: 88.0
# Letter Grade: B



# Create a function print_pattern that takes 
# an integer n and prints a pattern of asterisks. 

# def print_pattern(n):
#     for i in range(1, n+1):
#         print("*" * i)

# print_pattern(3)
# print_pattern(6)

#
# Write a function is_even that takes an integer 
# as a parameter and returns True if it's even, 
# False otherwise.
#
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(4.0))
# print(is_even(5.9))



# Define a function calculate_average that takes 
# three parameters (grades) and returns their average.

# def calculate_average(grade1,grade2,grade3):
#     average = (grade1 + grade2 + grade3) / 3
#     return average

# print(calculate_average(6,5,4))
# print(calculate_average(7.5,22,15.7))


# def calculate_area(radius):
#     # 1 is the function name and definition
#     # 2 is the paramater (above)
#     # 3 is the code block below
#     pi = 3.14
#     area = pi * radius ** 2
#     # 4 is the return value
#     return area
    
# value = calculate_area(5)
# print("The area of the circle is", value )

# print(calculate_area(6))


#  Write a function that will test if an input is a integer
# it must say if it is or is not a number

# def number_test(usernum):
#     '''
#     Parameters
#     ----------
#     usernum : get a number
#         This will be an integer, float or not a number

#     Returns
#     -------
#     None.

#     '''
    
#     try:
#         float(usernum)
#         try:
#             int(usernum)
#             print(f"'{usernum}' is a integer")
#         except:
#             print(f"'{usernum}' is a float")
#     except:
#         print(f"'{usernum}' is not a number")


# number_test("12")
# number_test("It's a boy")
# number_test("27")
# number_test("")
# number_test("12.5")   # needs to show as a float
# number_test("-5")
# number_test("0")

# help(number_test)





# =============================================================================
# 
# ### Homework
# # Write the dice roller so it asks 
# # how many sides to roll, 
# # how many of each dice type to roll
# # and continue asking until they stop
# # e.g. roll 2 x 10 sided dice, 4 x 6 sided, 1 x 20 sided
# 
# 
# '''
# Create a Python program that simulates rolling a dice (e.g., a standard six-sided die).
# The program should generate a random number between 1 and 6 to mimic the roll of a die.
# 
# Ask the user how many sides they want on the dice
# '''
# 
# 
# import random
# 
# total = 0
# 
# def roll_dice():
#     '''
#     
# 
#     Returns
#     -------
#     total : int
#         This is the total of the dice rolls
# 
#     '''
#     global total
#     total_rolls = len(user_dice)
#     dice_pos = 0
#     while dice_pos < total_rolls:
#         for each in user_rolls:
#             #print(f"dice rolls position is {dice_pos}")
#             while each > 0:
#                 each = each -1
#                 #print(f"user_dice {dice}")
#                 #print(f"the number of roll is {each}")
#                 num = random.randint(1, user_dice[dice_pos])
#                 print(f"you rolled a {num} out of {user_dice[dice_pos]}")
#                 total = total + num
#             dice_pos = dice_pos + 1
#         
#     #print("Total = ", total)
#     return total
#         
#    
#             
# 
# user_dice = []
# user_rolls = []
# 
# while True:
#     sides = input("Press 'X' to exit\nHow many sides for a dice to roll: ")
#     if sides.lower() == 'x':
#         break
#     else:
#         try:
#             sides = int(sides)
#             while True:
#                 rolls = input(f"How many rolls of {sides} sided dice to roll: ")
#                 if rolls.lower() == 'x':
#                     break
#                 else:
#                     try:
#                         rolls = int(rolls)
#                         user_rolls.append(rolls)
#                         user_dice.append(sides)
#                         break
#                     except:
#                         print("invalid number. Please give number of rolls again")           
#         except:
#             print("Invalid number. Try again")
#     
# # print("User dice is ", len(user_dice))
# 
# roll_dice()
# print(f"You rolled a total of {total}")
# 
# =============================================================================
