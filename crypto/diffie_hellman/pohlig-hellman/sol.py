#!/usr/bin/sage

from Crypto.Util.number import *

def pohlig_hellman(p , g , h , N = list):
    
    """
    Usage :
    h = g**x % p
    
    If known factors of p , put into N as prime_list

    """

    F = IntegerModRing(p)
    g = F(g)
    h = F(h)
    G = []
    H = []
    X = []
    c = []
    
    if not N:
        N = factor(p - 1)

    for i in range(0,len(N)):
        G.append(g ** ((p-1) / (N[i][0] ** N[i][1])))
        H.append(h ** ((p-1) / (N[i][0] ** N[i][1])))
        X.append(log(H[i] , G[i]))
        c.append((X[i] , (N[i][0] ** N[i][1])))

    print("G = {}\nH = {}\nX = {}".format(G , H , X))

    c.reverse()

    for i in range(len(c)):
        if len(c) < 2:
            break

        t1 = c.pop()
        t2 = c.pop()
        r = crt(t1[0] , t2[0] , t1[1] , t2[1])
        m = t1[1] * t2[1]
        c.append((r , m))

    return ("(x,p-1) =",c[0])


if __name__ == "__main__":

    x , p_1 = pohlig_hellman(p , g , h , prime_list) 
    print(long_to_bytes(x))
