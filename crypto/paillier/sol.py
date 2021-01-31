#!/usr/bin/python3

from gmpy2 import *
from Crypto.Util.number import *

n =
g = 
c =

p =
q = n // p

assert q * p == n

def l(x , n):
    return (x - 1) // n

lamd = lcm(p - 1 , q - 1)

mu = invert(l(pow(g , lamd , n ** 2) , n) , n)
flag = l(pow(c , lamd , n  ** 2) , n) * mu % n

print(long_to_bytes(pow(c , d , n)).decode())

