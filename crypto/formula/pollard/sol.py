#!/usr/bin/python3
from gmpy2 import gcd

def pollard(n):
    a = 2
    b = 2
    while 1 :
        a = pow(a , b , n)
        d = gcd(a - 1 , n)
        if 1 < d < n :
            return d
        b += 1

n =
primes= []

while(pollard(n) > 1):
    primes.append(pollard(n))

phi = 1

for i in primes:
    phi *= (i - 1)


