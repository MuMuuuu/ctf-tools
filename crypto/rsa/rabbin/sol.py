#!/usr/bin/python3
from Crypto.Util.number import *
from gmpy2 import *

e = 2
n = 
c =

p = n // q
assert p * q == n 

mp = pow(c , (p + 1) / 4 , p)
mq = pow(c , (q + 1) / 4 , q)
yp = invert(p , q)
yq = invert(q , p)

r = (yp * p * mq + yq * q * mp) % n
rr = n - r
s = (yq * q * mp + yp * p * mq) % n
ss = n - s

print("\n".join(map(lambda i : long_to_bytes(i).decode("latin-1") . [r , rr , s , ss])))

