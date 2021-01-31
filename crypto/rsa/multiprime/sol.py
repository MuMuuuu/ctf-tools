#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

n = 
e = 
c = 
primes = []

phi = 1
for i in primes:
    phi *= (i - 1)

print(long_to_bytes(pow(c , invert(e , phi) , n )).decode("latin-1"))
