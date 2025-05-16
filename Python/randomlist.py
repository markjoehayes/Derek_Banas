#!/usr/bin/python3

# Create a random list with 5 random values between 1 and 9

import random

r_list = []
for i in range(6):
    r_list.append(random.randint(0,9))
print(r_list)

