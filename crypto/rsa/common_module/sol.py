#!/usr/bin/python3
from gmpy2 import * # import gcdext as egcd 
from Crypto.Util.number import *

#(e1 * a) + (e2 * b) = gcd(e1, e2)
def egcd(a , b):
    if a == 0:
        return (b , 0 , 1)
    else:
        g , y , x = egcd(b % a , a)
        return (g ,x - (b // a) * y , y)

n =
e1 = 
e2 = 
c1 = 
c2 = 

_ , s1 , s2 = egcd(e1 , e2)

if s1 < 0: 
    s1 = abs(s1)
    c1 = invert(c1 , n)

elif s2 < 0:
    s2 = abs(s2)
    c2 = invert(c2 , n)

flag = pow(c1 , s1 , n) * pow(c2 , s2 , n) % n

print(long_to_bytes(flag).decode("latin-1"))
