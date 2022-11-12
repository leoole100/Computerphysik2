#!/usr/bin/env python3

##
# @file 1i.py
# @brief calculate the determinant of a 2x2 matrix. use it to calculate the determinant of an NxN matrix

import random

# Matrix = 2-dimensional list [[a,b],[c,d]]
def det_2x2(M):
    # det(M) = ad - bc
    return M[0][0]*M[1][1] - M[1][0]*M[0][1]

# determinant of NxN matrix by laplace theorem
def det_NxN(M):
    if len(M) == 2:
        return det_2x2(M)
    result = 0
    for i in range(0,len(M)):
        M_new = [z[:i] + z[i+1:] for z in M[1:]]
        result += (-1)**i * M[i][0] * det_NxN(M_new)
    return result

# try some examples

example_Ms = [[[1,2],[3,4]], [[1,2,3],[4,5,6],[7,8,9]], [[1,0,0],[0,1,0],[0,1,1]],[[1,0],[0,1]]]


# now generate random matrix of dimension n by n
n = 11 # takes long, but eventually completes. should not go higher than 11

M_test = []

for i in range(0,n):
    M_test = M_test + [[]]
    for j in range(0,n):
        M_test[i] = M_test[i] + [random.random() * 9.9]
        

# append randomly generated matrix to list of test matrices
example_Ms = example_Ms + [M_test]

for M in example_Ms:
    print("")
    for i in range(0,len(M)):
        
        if int(len(M) / 2) == i:
            print("det(M) = |", end="")
        else:
            print("         |",end="")
        for j in range(0,len(M)):
            print(" %.1f " % M[i][j], end="")
        print("|", end="")
        if int(len(M) / 2) == i:
            print(" = %f" % det_NxN(M), end="")
        print("")
        
print("\nHave a nice day.")
