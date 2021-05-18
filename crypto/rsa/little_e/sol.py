#!/usr/bin/python3
from gmpy2 import *
from Crypto.Util.number import *

n = 
e = 
c = 

def small(e , n , c):
    for k in range(20000000):
        res = iroot(c + n * k , e)
        if res[1]:
            print("Success ! \n")
            return res[0]

flag = small(e , n , c)

if flag == None:
    print("Not find little e")
    exit()
else:
    print(flag)
    print(long_to_bytes(flag))

