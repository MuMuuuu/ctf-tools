#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

e = 
n1 =
n2 = 
c =

assert n2 > n1

pq = (n2 - n1 - 4) // 2
phi1 = n1 - pq + 1
phi2 = n1 + pq + 1

d1 = invert(e , phi1)
d2 = invert(e , phi2)

print(long_to_bytes(pow(c , d1 , n1)))
print(long_to_bytes(pow(c , d2 , n2)))
print(long_to_bytes(pow(pow(c , d2 , n2) , d1 , n1)))
print(long_to_bytes(pow(pow(c , d1 , n1) , d2 , n2)))
