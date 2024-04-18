#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:13:09 2024

@author: marcus
"""

### Temperature Converter
# F to C = -32 * 5/9
# C to F = * 5/9 + 32

def celsius_to_fahrenheit(celsius):
    return round((celsius *9/5) +32 ,2)

def fahrenheit_to_celsius(fahrenheit):
    output = ((fahrenheit -32) * 5/9)
    return(round(output,2))

user_choice = input("Enter 'C' for Celsius to Fahrenheit, \
                    or 'F' for Fahrenheit to Celsius \
                        Choice: ")

if user_choice.lower() == "c":
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
elif user_choice.lower() == 'f':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
else:
    print("Invalid choice.")
    



## Prime number checker
#user_input = int(input("Give me a number: "))
# =============================================================================
# 
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# 
# # if is_prime(user_input):
# #     print(f"{user_input} is a prime number!")
# # else:
# #     print(f"{user_input} is not a prime number.")
# 
# assert is_prime(11) == True, "11 is a prime" # expect T
# assert is_prime(12) == False, "12 is not a prime" # False
# 
# =============================================================================
## Palindrome checker
# =============================================================================
# 
# def is_palindrome(s):
#     s = s.lower().replace(" ","") # remove spaces and capitals
#     return s == s[::-1]
# 
# user_input = input("Enter a string: ")
# 
# if is_palindrome(user_input):
#     print(f"{user_input} is a palindrome")
# else:
#     print(f"{user_input} is NOT a palindrome")
# 
# 
# =============================================================================
# =============================================================================
# user_input = input("Gime something: ")
# 
# print(user_input)
# print(user_input[:4])  # up to position 4
# print(user_input[1:4]) # from pos 1 to 4 
# print(user_input[4::2])  # from pos 4
# print(user_input[::-1])  
# 
# if user_input == user_input[::-1]:
#     print("It's reversable")
# =============================================================================
