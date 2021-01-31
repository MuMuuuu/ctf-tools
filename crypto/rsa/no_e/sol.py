#!/usr/bin/python3
from string import printable
from gmpy2 import *
from Crypto.Utli.number import *

### chall gives a list for encrypted flag 

n = 
c = 
p = 
q = n // p

assert p * q == n

phi = (q - 1) * (p - 1)

for e in range(10000):
    d = invert(e , phi)
    if long_to_bytes(pow(c , d , n)) in printable:
        true_e = e
        break

flag = ""
for c in ls:
    flag += long_to_bytes(pow(c , d , n))

print(flag)
