#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:37:40 2024

@author: marcus
"""

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

import string

vowel_list = "aeiouAEIOU"
vlist = ['a', 'i', 'e']

vowels = 0
consonants = 0
numbers = 0
special = 0
spaces = 0

words = 0

text = "the 5 Brown fox's ate 17 of my F&*^'n chickens!"

# user_text = input("What do you want to check: ")
user_text = text

for each in text:
    if each.lower() in vowel_list:
        #print(each, "is in the string letter list")
        vowels += 1      
    #elif each.lower() in string.ascii_lowercase and each.lower() not in "aeiou":
    #    consonants += 1
    elif each in string.digits:
        #print(each, "is a digit")
        numbers += 1
    elif each in string.punctuation:
        # print(each, "is in the punctuation list")
        special += 1
        # special = special + 1
    elif each in string.whitespace:
        #print(each, "is a whitespace")
        spaces += 1
    else:
        #print(each, "is some weird letter")
        consonants += 1


print(f"There are {vowels} vowels")
print("There are " + str(consonants) + " consonants")
print("There are", numbers, "numbers")
print(f"There are {special} special characters")
print(f"There are {spaces} spaces")

print(f"There are {words} words")

