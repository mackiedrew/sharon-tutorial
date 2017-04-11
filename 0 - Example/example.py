#!/usr/bin/python

##### Input #####
value_to_test = 5


##### Processing #####

# The modulus operator (%) divides a number and then outputs the remainder
# In this case we are dividing the value by two
remainder = value_to_test % 2

# If a number divided by 2 has a remainder, then it must be odd.
# 1 % 2 = 1
# 2 % 2 = 0
# 3 % 2 = 1
# 4 % 2 = 0
# 5 % 2 = 1

if remainder == 0:
    even = True
else: 
    even = False


##### Output #####
if even:
    print("The value is even.")
else:
    print("The value is odd.")
