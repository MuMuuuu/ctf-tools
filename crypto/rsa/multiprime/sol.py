#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

def parser(s:str):
    return list(map(int , s.strip().split(" * ")))


n = 
e = 
c = 

a = """ """ # input factor result
primes = parser(a)

phi = 1
for i in primes:
    phi *= (i - 1)

print(long_to_bytes(pow(c , invert(e , phi) , n )).decode("latin-1"))
