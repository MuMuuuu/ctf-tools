#!/usr/bin/python3

from gmpy2 import isqrt , is_square

def fermat(n):
    a = isqrt(n) + 1

    while not is_square(pow(a , 2) - n):
        a += 1

    b = isqrt(pow(a , 2) - n)
    p = a + b
    q = a - b

    assert p * q == n

    return p , q

n = int(input("n = ")) # input n

p , q = fermat(n)

print(f"n = {n}\np = {p}\nq = {q}")

