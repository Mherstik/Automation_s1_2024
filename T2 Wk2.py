#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:10:56 2024

@author: marcus
"""


import os
import csv
import platform
import sys

# import speedtest-cli

c = os.getcwd()
#print(c)

filename = input("What name for the file: ")

# remove file4 if it exists
if os.path.exists(filename):
    print(f"{filename} exists... removing!!")
    os.remove(filename)
else:
    print(f"{filename} is not found\
          \nCreating {filename}") # print(x)



#f = open('file3.csv', 'r') # open for reading
#print(f.read(5))
#print(f.readlines(3))


# open for appending
f = open(filename, "a")
f.write("\nJane, 10")
f.close()

# f = open(filename, 'r')
# print(f.read())


# with open(filename, 'r') as f:
#     print(f.read())
    
with open(filename, 'w', newline='') as csvfile:
    somewriter = csv.writer(csvfile, delimiter=' ')
    somewriter.writerow("Computer_Name,IP-address,MAC-address,Processor_Model,Operation System,System time,Internet connection speed,Active ports")

with open(filename, newline='') as csvreader:
    somereader = csv.reader(csvreader, delimiter=" ")
    for row in somereader:
        print(''.join(row))




print(os.name)
print(platform.system())
print(platform.release())
print(sys.platform)


import urllib.request
import time

def check_speed(url="http://speedtest.ftp.otenet.gr/files/test10Mb.db"):
    start_time = time.time()
    with urllib.request.urlopen(url) as response:
        response.read()
    end_time = time.time()
    speed = (10 * 1024) / (end_time - start_time)  # Convert bytes to megabits and calculate speed
    return speed

speed = check_speed()
print(f"Download speed: {speed:.2f} Mbps")


##########
# Speedtest CLI
import sys
import subprocess
import pkg_resources

required = {'speedtest-cli', 'psutil'}
#required = {'psutil'}
installed = {pkg.key for pkg in pkg_resources.working_set}

#print(required)
#print(installed)
missing = required - installed

if len(missing) > 0:
    print(f"{missing} is missing")
    
#print(missing)
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)    

import speedtest
servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
download_speed = s.download(threads=threads)
upload_speed = s.upload(threads=threads)
print(download_speed /1024/1024, upload_speed/1024/1024)
s.results.share()

results_dict = s.results.dict()