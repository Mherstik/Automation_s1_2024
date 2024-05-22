#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:29:16 2024

Purpose: Read data from a file and check if 
there is duplicate information on a line


@author: marcus
"""

import sys
import csv

fname = "T2Wk6.csv"

with open(fname, newline='') as csvfile:
    readDuplicate = csv.reader(csvfile, delimiter=',')
    dataList = list(readDuplicate)
    n = len(list(dataList))
    print(f"{n} records in list")
    if n < 3:
        print("Not enough data")
        #continue
        #break
        sys.exit()
    x = 2
    while x < n:
        if dataList[x][0] == dataList[x-1][0]: # check for duplicate
            print(f"Line {x} has {dataList[x-1][0]}, {dataList[x-1][1]}, {dataList[x-1][2]} is same as \
                  {dataList[x][0]},{dataList[x-1][1]}, {dataList[x][2]}")
            x = x + 2
        else:
            print(f"Line {x} is {dataList[x-1][0]}, {dataList[x-1][1]}, {dataList[x-1][2]}")
            x = x + 1

#print(dataList)
# i = 0
# for each in dataList:
#     #print(type(each))    
#     print(each[1]) #, "is in index", i)
#     #i += 1
    
    
    

# f = open(fname, 'r')
# ex1 = f.readline()
# ex2 = f.readlines()

# print("Ex1 is", ex1)
# print("Ex2 is", ex2)
# f.close()
#readList = f.readlines()
#print(type(readList))


# userChoice = input("Give me a 3 digit number: ")

# fname = 'T2Wk6.txt'
# f = open(fname, 'r')
# #print(f.read())
# #print("-----------")

# ex1 = f.readline()
# ex2 = f.readlines()

# print(ex1)
# print(ex2)
# #readList = f.readlines()
# #print(type(readList))

# #for x in f:
# #    print(x)
# f.close()

# # using a set to check values
# with open (fname) as f:
#     seen = set()
#     for line in f:
#         # convert case
#         line_lower = line.lower() # optional
#         if line_lower in seen:
# #for x in file:
# #    if x == userChoice:
#             print(line_lower, 'is in the file already')
#         else:
#             print(line_lower, 'is NOT in the file already')
#             seen.add(line_lower)
# f.close()
# print("Seen is", seen)

# myList = [5,3,5,1,2,7,8]
# newList = []
# print(myList)
# print("My list length is:", len(myList))

# mySet = set(myList)
# print(mySet)
# print("My set length is:", len(mySet))

# for each in myList:
#     #print(each)
#     if each in newList:
#         print(each, "is in the list")
#     else:
#         print(each, "only appears once")
#         newList.append(each)
# print(newList)
    
    
    
