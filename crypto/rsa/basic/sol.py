#!/usr/bin/python3
from Crypto.Util.number import *

e = 
n = 
c =

p =
q = n // p
assert p * q == n

phi = (q - 1) * (p - 1)
d = inverse(e , phi)

print(long_to_bytes(pow(c , d , n)).decode("latin-1"))
