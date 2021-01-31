#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

n = 
e = 
c = 


def small(e , n , c):
    for k in range(20000000):
        if iroot(c + n * k , e)[1]:
            print("Success ! \n")
            return iroot(c + n * k , 3)

flag = small(e , n , c)
print(flag)

print(long_to_bytes(flag))
