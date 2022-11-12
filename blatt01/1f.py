#!/usr/bin/env python3

##
# @file 1f.py
# @brief convert complex numbers between polar and cartesian form
# @author aurel mueller-schoenau and leon oleschko

import math

def polar_to_complex(z):
    x = z[0] * math.cos(z[1])
    y = z[0] * math.sin(z[1])
    return (x,y)
        
def complex_to_polar(z):
    r = math.sqrt(z[0]**2 + z[1]**2)
    phi = math.atan2( z[1], z[0])
    return (r,phi)


# try it for some examples

examples_polar = [(12,1.4), (2.2,0.1), (8, -0.3)]
examples_complex = [(1,0), (1,3), (2,-0.4), (-3,2.2)]

print("\nSome numbers in polar form converted to cartesian coordinates:")
for z in examples_polar:
    print("\nR= %f, phi= %f converts to %f + %fi" %  (z + polar_to_complex(z)))

print("\n\nAnd here are some numbers converted from cartesian to polar:")

for z in examples_complex:
    print("\n%f + %fi converts to R= %f, phi= %f" % (z + complex_to_polar(z)))
	
print("\nHave a nice day.")
