n =
e = 
c = 

beta = 1
epsilon = beta ^ 2/7

nbits = n.nbits()
kbits = floor(nbits * (beta ^ 2 / e - epsilon))
mbar = m & (2 ^ nbits - 2 ^ kbits)

PR.<x> = PolynomialRing(Zmod(n))
f = (mbar + x) ^ e - c

print(m)
x0 = f.small_roots(X = 2 ^ kbits , beta = 1)[0]

from pyCrypto.Util.number import long_to_bytes

print(mbar + x0)
print(long_to_bytes(mbar + x0))
