#!/usr/bin/python3

from functools import reduce

def gcd(a , b):
    a , b = abs(a) , abs(b)
    if b == 0:
        return a
    else:
        return gcd(b , a % b)

def ext_gcd(a , b):
    if a == 0:
        return (b , 0 , 1)
    else:
        g, x, y = ext_gcd(b % a , a)
        return (g , y - (b // a) * x , x)

def invert(a , n):
    a = a % n
    g, x, _ = ext_gcd(a , n)
    if g == 1:
        return x % n
    else:
        raise Exception("None of inverse exist")

def find_inc(states , mod , mul):
    s0 , s1 = states[:2]
    inc = (s1 - (s0 * mul)) % mod
    return inc

def find_mul(states , mod):
    s0 , s1 , s2 = states[:3]
    mul = (s2 - s1) * invert(s1 - s0 , mod)
    return mul % mod

def find_mod(states):
    subs = [b - a for a , b in zip(states , states[1:])]
    zero = [t2 * t0 - t1 * t1 for t0 , t1 , t2 in zip(subs[:-2] , subs[1:-1] , subs[2:])]
    mod = reduce(lambda a , b : gcd(a , b) , zero)
    return mod

def next_state(state , mod , mul , inc):
    return (state * mul + inc) % mod

def get_all(states , mod=0 , mul=0 , inc=0 , init=0):
    """
    states: list of states
    mod: mod of LCG
    mul: mul of LCG
    inc: inc of LCG
    init: initial state of LCG

    Formula should be (init * mul + inc) % mod
    ``If initial state is given , first yield will be initial``.

    """
    if mod == 0:
        mod = find_mod(states)
    if mul == 0:
        mul = find_mul(states , mod)
    if inc == 0:
        inc = find_inc(states , mod , mul)

    assert (states[0] * mul + inc) % mod == states[1]

    if init == 0:
        state = states[-1]
        while True:
            state = next_state(state , mod , mul , inc)
            yield state
        
    else:
        state = init
        while True:
            yield state
            state = next_state(state , mod , mul , inc)

