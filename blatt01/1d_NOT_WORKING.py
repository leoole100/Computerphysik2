#!/usr/bin/env python3

##
# @file 1d.py
# @brief try to find the largest integer number python can operate with

# Not working

n = 0
while(isinstance(n,int)):
    print("Trying %d... Passed!\n" % n)
    n = (n << 1) + 1
print("The greatest number assignable to an int is %d" % n)
	
print("\nHave a nice day.")
