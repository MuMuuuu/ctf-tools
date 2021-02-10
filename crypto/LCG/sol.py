#!/usr/bin/python3
from gmpy2 import *
from functools import reduce
import math

def _crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def _crack_unknown_multiplier(states, modulus):
    a = (states[2] - states[1])
    inv = int(invert(states[1]-states[0] % modulus, modulus))
    multiplier = (a * inv) % modulus
    return _crack_unknown_increment(states, modulus, multiplier)

def _crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:],diffs[2:])]
    modulus = abs(reduce(lambda x,y: math.gcd(x,y),zeroes))
    return _crack_unknown_multiplier(states, modulus)

def crack(seq):
    return _crack_unknown_modulus(seq)

def next_state(s0 , m , inc , n):
    return (m * s0 + inc) % n

ls = []

seed = ls[0]
new = [seed]
n , m , inc = crack(ls)

assert next_state(seed , m , inc , n) == ls[1]

for i in range(100):
    seed = next_state(seed , m , inc , n)
    new.append(seed)


