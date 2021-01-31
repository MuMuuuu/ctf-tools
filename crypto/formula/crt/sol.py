#!/usr/bin/python3
from gmpy2 import *
from functools import reduce

def CRT(r, mod):
    M = reduce(lambda x,y:x*y, mod)

    ans = 0
    
    for i in range(len(r)):
        m = M // mod[i]
        ans += r[i] * m * gmpy2.invert(m, mod[i])
    
    return ans % M

n = []
c = []
e = 

m = CRT(c , n)
print(long_to_bytes(iroot(m , e)[0]).decode("latin-1"))