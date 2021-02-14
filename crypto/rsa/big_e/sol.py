#!/usr/bin/python3

from owiener import attack
from Crypto.Util.number import *

n = 
c = 
e = 

d = attack(e , n)

print(long_to_bytes(pow(c , d , n)).decode("latin-1"))
