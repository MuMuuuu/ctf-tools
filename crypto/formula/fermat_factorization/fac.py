#!/usr/bin/python3

from gmpy2 import isqrt

def fermat(n):
    t0 = isqrt(n) + 1
    counter = 0
    t = t0 + counter
    tmp = isqrt(pow(t , 2) - n)

    while(pow(tmp , 2) != pow(t , 2) - n):
        counter += 1
        t = t0 + counter
        tmp = isqrt(pow(t , 2) - n)

    p = t + tmp
    q = t - tmp

    return p , q

n = int( ) # input n

p , q = fermat(n)

print(f"p = {p}\nq = {q}")

