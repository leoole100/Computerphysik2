#!/usr/bin/env python3

##
# @file 1h.py
# @brief calculate the cross product of two vectors
# @author aurel mueller-schoenau and leon oleschko

import math
import itertools

def cross_prod(u,v):
    u,v = tuple(u)*2, tuple(v)*2
    result = []
    for i in range(0,3):
        result = result + [u[i+1]*v[i+2] - u[i+2]*v[i+1]]
    return tuple(result)

# input two vectors

print("Calculate cross product:\n")
      
vectors = [[],[]]

for j in range(0,2):
    print("\nVector #%d:\n" % (j+1))
    i = 0
    while i < 3:
        try:
            vectors[j] = vectors[j] + [float(input("Input x_%d-coordinate: " % i))]
            i = i+1
        except ValueError:
            print("please enter a valid number\n")

print("\n\nCross Product:\n")
print("(%f, %f, %f) x (%f, %f, %f) = (%f, %f, %f)" % (tuple(vectors[0]) + tuple(vectors[1]) + cross_prod(vectors[0],vectors[1])))
	
print("\nHave a nice day.")
