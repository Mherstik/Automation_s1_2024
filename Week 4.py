#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:37:40 2024

@author: marcus
"""


'''
Create a Python program that simulates rolling a dice (e.g., a standard six-sided die).
The program should generate a random number between 1 and 6 to mimic the roll of a die.

Ask the user how many sides they want on the dice
'''

import random

def diceroll():
    roll = random.randint(1,6)
    return roll


print("Rolling the dice....")
print("You rolled a", diceroll())

print("You rolled a", diceroll())

print("You rolled a", diceroll())


### HOMEWORK  ###

# get input from a user
# count how many vowels, consonants, 
# numbers and special characters are in it/
# eg. input = "the 5 Brown fox's ate 17 of my F&*^'n chickens!"
# eg. output  
# 21 consonants
# 8 vowels
# 3 numbers
# 6 special characters
# 9 spaces (optional)

## Import modules!!

# import string

# vowel_list = "aeiouAEIOU"
# vlist = ['a', 'i', 'e']

# vowels = 0
# consonants = 0
# numbers = 0
# special = 0
# spaces = 0

# words = 0

# text = "the 5 Brown fox's ate 17 of my F&*^'n chickens!"

# # user_text = input("What do you want to check: ")
# user_text = text

# for each in text:
#     if each.lower() in vowel_list:
#         #print(each, "is in the string letter list")
#         vowels += 1      
#     #elif each.lower() in string.ascii_lowercase and each.lower() not in "aeiou":
#     #    consonants += 1
#     elif each in string.digits:
#         #print(each, "is a digit")
#         numbers += 1
#     elif each in string.punctuation:
#         # print(each, "is in the punctuation list")
#         special += 1
#         # special = special + 1
#     elif each in string.whitespace:
#         #print(each, "is a whitespace")
#         spaces += 1
#     else:
#         #print(each, "is some weird letter")
#         consonants += 1

# print(text)
# print(f"There are {vowels} vowels")
# print("There are " + str(consonants) + " consonants")
# print("There are", numbers, "numbers")
# print(f"There are {special} special characters")
# print(f"There are {spaces} spaces")

# text2 =[]
# word_count = 0
# for each in text.split():
#     text2.append(each)
# print(text2)


# # for each in text2:
# #     if each in string.digits:
# #         print(f"{each} is a digit")
# #         continue    
# #     else:
# #         print(f"{each} is a word")
# #         word_count += 1

# # for each in text2:
# #     int(each)

# for each in text2:
#    try:
#        int(each)
#    except:    
#        word_count += 1
       
       
# num = len(text.split())
# words = num - numbers
# print(f"There are {num} words using split")
# print(f"There are {words} words using split - numbers")
# print(f"There are {word_count} words using a split and then check for numbers")


