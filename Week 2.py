#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:27:39 2024

@author: marcus
"""

fname = input("What is your first name? ")

num = input("Give me a number: ")
#num = float(num)

if fname == "Marcus":
    print(f"Hello {fname}")
else:
    print("Get off my lawn")

## Test if it's really a number
# if num.isdecimal():
#     print("It's a decimal")
# elif num.isdigit():
#     print("It's a number")
# elif num.isalnum() or num.isspace():
#     print("It's alpha numeric")
# else:
#     print("It's nothing good")

## num is stored as string
## Change the num variable to an integer
# print("num is stored as", type(num))
# num = float(num)
# print("num is stored as", type(num))
# num = int(num)
# print("num is stored as", type(num))
#num = float(num)

# print("Hello " + fname)
# print("Hello", fname)

# print("The next number is", num + 1)
# print("The next number is " + str(num + 1) )

# print(f"The next number is {num + 1}")
# print(f'The next number is {num + 1}')
# print(f"My name is {fname} and I am {num + 1} years old next year.")


 
# a = 1
# b = 2.0
# c = "test"

# print("a is", type(a))
# print("b is", type(b))
# print("c is", type(c))

# a = float(a)
# b = int(b)
# #c = int(c)

# print("a is", type(a))
# print("b is", type(b))
# print("c is", type(c))

