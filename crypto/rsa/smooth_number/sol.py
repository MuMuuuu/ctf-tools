#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

def pollard_bf(n):
    a = 2
    b = 1
    while 1:
        a = pow(a , b, n)
        if 0 < gcd(a - 1 , n) < n:
            return gcd(a - 1 , n)
        b += 1

n = 
e = 
c = 

p = pollard_bf(n)

q = n // p
assert p * q == n

print(long_to_bytes(pow(c , invert(e , (q - 1) * (p - 1)) , n)))
