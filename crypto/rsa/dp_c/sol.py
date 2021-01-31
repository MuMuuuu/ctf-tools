#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

dp = 
e = 
c = 
n = 

for i in range(1 , e):
    p = (e * dp - 1) // i + 1
    if n % p == 0:
        break 
    else:
        continue


q = n // p
d = invert(e , (p - 1) * (q - 1))

print(long_to_bytes(pow(c , d , n)).decode())
