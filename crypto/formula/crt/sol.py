#!/usr/bin/python3

from gmpy2 import invert , iroot
from functools import reduce
from Crypto.Util.number import long_to_bytes

def CRT(r, mod):
    M = reduce(lambda x , y : x * y , mod)

    ans = 0
    
    for i in range(len(r)):
        m = M // mod[i]
        ans += r[i] * m * invert(m , mod[i])
    
    return ans % M

n = []
c = []
e = len(n)

m = CRT(c , n)
print(long_to_bytes(iroot(m , e)[0]).decode("latin-1"))
