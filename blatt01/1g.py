#!/usr/bin/env python3

##
# @file 1g.py
# @brief calculate norm of a vector and the normalized vector

import math

def normalise(v):
    norm = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    if(norm == 0):
        return (norm, (0,0,0))
    else:
        x = v[0] / norm
        y = v[1] / norm
        z = v[2] / norm
        return (norm, x,y,z)

# let the user input a vector and return the normalised vector

print("Normalise a vector:\n")

v = []
i = 0
while i < 3:
    try:
        v = v + [float(input("Input x_%d-coordinate: " % i))]
        i = i+1
    except ValueError:
        print("please enter a valid number\n")

print("\nYou entered the vector (%d, %d, %d)\n" % tuple(v))
print("The norm of your vector is %f.\n\nThe normalised vector is (%f, %f, %f)" % normalise(v))
	
print("\nHave a nice day.")
