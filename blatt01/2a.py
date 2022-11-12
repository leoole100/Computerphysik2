#!/usr/bin/env python3

##
# @file 2a.py
# @brief implement factorial in different ways and compare the performance
# @author aurel mueller-schoenau and leon oleschko

import time
import math

from more_itertools import tabulate

def factorial_recursive(n):
	'''
		@note throws RecursionError at n >= 998
	'''
	if n == 0:
		return 1
	return n * factorial_recursive(n - 1)

def factorial_iterative(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

def factorial_tail_recursive(n, result = 1):
	if n == 0:
		return result
	return factorial_tail_recursive(n - 1, result * n)

def factorial_math(n):
	return math.factorial(n)


# factorial functions
factorial_functions = [factorial_recursive, factorial_iterative, factorial_tail_recursive, factorial_math]

# compare correctness
for factorial_function in factorial_functions:
	for i in range(0, 100):
		try:
			assert factorial_function(i) == math.factorial(i)
		except AssertionError:
			print("  %s is incorrect at %d" % (factorial_function.__name__, i))
			exit(1)
		except RecursionError:
			print("  %s throws recursion error at %d" % (factorial_function.__name__, i))
			exit(1)

print("All factorial functions are correct.")

# compare performance
print("Comparing performance of factorial functions:")
for factorial_function in factorial_functions:
	start_time = time.time()
	for i in range(0, 100):
		factorial_function(i)
	end_time = time.time()
	print("   %s: %.2g ms" % (factorial_function.__name__, (end_time - start_time) * 1000))
