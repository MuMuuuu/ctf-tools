#!/usr/bin/sage

"""
My SageMath is under python2
"""

from sage.all import *
from Crypto.Util.number import long_to_bytes

lst = continued_fraction(Integer(e) / Integer(n))
conv = lst.convergents()

e = 
n = 
c = 

format = " "

for i in conv:
    d = int(i.denominator())
    try:
        m = long_to_bytes(pow(c , d , n))
        if format.encode() in m:
            print(m.decode())
            break
    except:
        continue

