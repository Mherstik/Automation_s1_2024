#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:11:02 2024

@author: marcus
"""

# 4.1	The following Python script pings each host on a given network twice. 
# Modify the script to output only those hosts that are active.


## variables
pingType = ''
operatingSystem = ''

# Script to ping all IP addresses in a /24 subnet
import os

# Check the operating system and set ping to appropriate
#print(os.name)
def getOperatingSystem():
    global operatingSystem
    global pingType
    operatingSystem = os.name
    if operatingSystem == 'nt':
        # nt (aka Windows) uses n for count
        pingType = 'n'
    else:
        # posix used c for count
        pingType = 'c'
    return pingType, operatingSystem

getOperatingSystem()
print("Your OS type is", operatingSystem)
print("Pinging using", pingType)

active = []
search = "ttl"

network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(network)

# Iterate over all usable IPs in this subnet
for host in range (115, 122):
    print("\n---------------")
    print("Pinging " + network + "." + str(host))
    
    # remove the output of the command
    # response = os.system("ping -" + str(pingType) + "2 " + network + "." + str(host) + "> /dev/null")
    # build the command
    pingCommand = f"ping -{pingType} 2 {network}.{str(host)}"
    response = os.popen(pingCommand)
    for line in response.readlines():
        
        if "ttl" in line.lower():
            #print(line)
            active.append(host)

    #response = os.system("ping -" + str(pingType) + "2 " + network + "." + str(host))
    
    
    # check for error or not
   # if response == 0:
        #print(network + "." + str(host) + " is up" )
   #     active.append(host)
    #else:         
     #   print(network + "." + str(host) + " is down" )

print("\n _________")


for each in set(active):
    print(network + "." + str(each) + " is up.")





# 4.2	Write a program to conduct a passive attack on the network associated
# with the local organisation that you have carried out reconnaissance in 3.7. 
# The passive attack should reveal the open ports on the various host servers 
# in the organisation’s network.


## get ip addresses
## for each IP address scan the port
##

# 4.3	Write another program to retrieve information from one of the open 
# ports that you have identified above. Use appropriate protocols associated 
# with the port to access it.


## get an IP address and port
## read the banner message in the 