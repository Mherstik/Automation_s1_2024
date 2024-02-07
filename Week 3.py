#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:13:55 2024

@author: marcus
"""

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

## we want to find all numbers that are even!
print(951/2)
print("The remainder of 951 divided by 2", 951%2)
print("The modulus of 951 divided by 2", 951//2)
## we want to find all numbers that are odd!




# From Josh and ChatGPT
# sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Slice from index 1 to 5, taking every element 
# # (default step is 1)
# print(sequence[1:6])  # Output: [1, 2, 3, 4, 5]

# # Slice from the beginning to index 5
# print(sequence[:6])  # Output: [0, 1, 2, 3, 4, 5]

# # Slice from index 3 to the end of the list
# print(sequence[3:])  # Output: [3, 4, 5, 6, 7, 8, 9]

# # Slice the entire list with 
# # a step of 2 (every second element)
# print(sequence[::2])  # Output: [0, 2, 4, 6, 8]

# # Reverse the list
# print(sequence[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# name = "marcus"

# print(name[1:6:2])

# servers = ["server 1", "server 2", "server 3"]

# for name in servers:
#     print(name)

# print(servers[0:])
# print(servers[:0])
# print(servers[:1])
# print(servers[1:])

# i = 1
# # for loop
# for i in range(0,10):
#     i = i + 1
#     print(i)



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

# name = input("Give me your name please: ")


# # # Read score between 0 -100
# while True:
#     score = input("Give me your score: ")
#     if score.isdigit():
#         score = int(score)
#         #if score >= 0 and score <= 100:
#         if score in range(0,101):
#             break
#         else:
#             print("Not a valid number")
#     else:
#         print("Not a valid number")

# #score = input("Give me your score: ")
# try:
#     score = float(input("Enter the student's score (0-100): "))
#     if score < 0 or score > 100:
#         print("Invalid score. The score must be between 0 and 100.")
# except ValueError:
#     print("Invalid input. Please enter a numeric value for the score.")



# if score < 50:
#     print(name, "Failed")
# # if score between 50 and 64
# elif score >=50 and score <= 64:
#     print(name, "passed")
# # if score between 65 and 74
# elif score >=65 and score <= 74:
# 	print("Credit")
# # if score between 75 and 84
# elif score >=75 and score <= 84:
#  	print("Distinction")
# # if score above 85
# else: 
#     print("HD")
# # 	HD
# 	
