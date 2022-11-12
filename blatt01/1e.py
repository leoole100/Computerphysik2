#!/usr/bin/env python3

##
# @file 1e.py
# @brief find out whether a given number is prime

def is_prime(n):
    prime = True
    for i in range(2,n-1):
        fraction = n / i
        prime &= (fraction != int(fraction))
    return prime

# input a number and check whether it is prime
print("Enter a number to see if it is prime!\n")


while(True):
    try:
        n = int(input("Your Number: "))
    except ValueError:
        print("Have a nice day.")
        exit(0)
    if(is_prime(n)):
        print("CONGRATULATIONS, %d IS A PRIME NUMBER\n" % n)
    else:
        print("%d is not prime :( \n" % n)
    

