#!/usr/bin/python3
from gmpy import *
from Crypto.Util.number import *

n1 = 

n2 = 

n3 = 

c1 = 

c2 = 

c3 = 

e = 

N = n1 * n2 * n3
N1 = N // n1 
N2 = N // n2
N3 = N // n3

u1 = invert(N1 , n1)
u2 = invert(N2 , n2)
u3 = invert(N3 , n3)

m = (c1 * u1 * N1 + c2 * u2 * N2 + c3 * u3 * N3) % N

flag = int(root(m , e)[0])

print(long_to_bytes(flag))
