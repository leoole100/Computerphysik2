#!/usr/bin/env python3

##
# @file 1c.py
# @brief print a table containing temperatures from 1 to 100 degree celsius and the corresponding fahrenheit value
# @author aurel mueller-schoenau and leon oleschko

def degree_to_fahrenheit(T):
    return 9*T/5 + 32

# print numbers 1 through 42 once using each function

T_min = 0
T_max = 100

print("Here are the temperatures from %d to %d degree Celsius in Fahrenheit:\n" % (T_min, T_max))

for T in range(T_min,T_max+1):
    print("%d C = %d F" % (T, degree_to_fahrenheit(T)))
	
print("\nHave a nice day.")
