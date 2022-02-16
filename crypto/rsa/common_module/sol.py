#!/usr/bin/python3.8
from Crypto.Util.number import long_to_bytes

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

_ , s1 , s2 = map(int , egcd(e1 , e2))

flag = pow(c1 , s1 , n) * pow(c2 , s2 , n) % n

print(long_to_bytes(flag).decode("latin-1"))
