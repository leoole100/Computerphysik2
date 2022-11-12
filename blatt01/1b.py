#!/usr/bin/env python3

##
# @file 1b.py
# @brief return the numbers 1 through 42, once using a for loop and once using a while loop
# @author aurel mueller-schoenau and leon oleschko

def count_for(n):
    for i in range(1,n+1):
        print(i)
    return
        
def count_while(n):
    i = 1
    while i < n+1:
        print(i)
        i = i + 1
    return

# counting functions
counting_functions = [count_for, count_while]

# print numbers 1 through 42 once using each function

n = 42
print("The integers from 1 to %d are:\n" % n)
for counting_function in counting_functions:
	counting_function(n)
	print("")
	
print("Have a nice day.")
