#1/usr/bin/python3
from gmpy2 import *
from CRypto.Util.number import *

n = 
e = 
c =

p =
power =
assert p * q == n

phi = p ** (power - 1) * (p - 1)
d = invert(e , phi)

print(long_to_bytes(pow(c , d , n)))
