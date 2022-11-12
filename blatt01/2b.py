#!/usr/bin/env python3

##
# @file 2b.py
# @brief calculate and print pascals triangle
# @author aurel mueller-schoenau and leon oleschko

def pascal_row(old_row, n):
    if n==0:
        return
    new_row = [old_row[0]] + [old_row[i] + old_row[i+1] for i in range(0,len(old_row)-1)] + [old_row[-1]]
    print(" " * int(2 * n), end="")
    print(new_row)
    pascal_row(new_row,n-1)

# number of pascal triangle rows to print
n=20

# disclaimer
print("\nThis program is supposed to draw pascals triangle. It is really bad.\n\n")

pascal_row([1],n)

print("\nHave a nice day!")
