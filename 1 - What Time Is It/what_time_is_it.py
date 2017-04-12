#!/usr/bin/python

import math

# Your first assignment is to take a certain number of seconds, and tell me how many minutes, and
# seconds are in that amount of time. I have added some pieces of code to get you started, you
# just need to figure out how to find the number of minutes in the total_seconds, and then how
# many seconds are left after that.

# For example:
# 13 seconds = 0 minutes, 13 seconds
# 122 seconds = 2 minutes, 2 seconds
# 400 seconds = 6 minutes, 40 seconds

# TIP: You should know about the built-in function: math.floor() this will take the value you
# provide it with and make it into the lowest whole number. Kind of like rounding, but always
# rounding down.
# math.floor(23.3223) == 23
# math.floor(32.9999) == 32
# math.floor(0.92332) == 0

# Ask the user for input, when they enter a number the program runs
total_seconds = float(input("Enter a number of seconds: "))
# float(string) convert the provided value into an number

# I would start by figuring out how many minutes there are in the total seconds

minutes = 0 # How many minutes are in the total_seconds provided.
seconds = 0 # How many seconds are in the total_seconds provided, minus the seconds in minutes.

# Output results
print("That amount of time is: ")
print(str(minutes) + ':' + str(seconds))
# str(number) is a built-in function that converts a number to an string so you can print() it!