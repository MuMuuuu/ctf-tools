#!/usr/bin/sage

"""
My SageMath is under python2
"""

from Crypto.Util.number import long_to_bytes

e = 
n = 
c = 

lst = continued_fraction(Integer(e) / Integer(n))
conv = lst.convergents()

format = " " # Input flag format

for i in conv:
    d = int(i.denominator())
    try:
        m = long_to_bytes(pow(c , d , n))
        if format.encode() in m:
            print(m.decode())
            break
    except:
        continue

