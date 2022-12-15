#!/usr/bin/python3.8

def rail_fence(pt , key):
    loop = (key - 1) * 2

    tmp = [[] for _ in range(key)]
    tmp[0].append(pt[0])
    down = False

    for i in range(1 , len(pt)):

        out = (loop - (i * [-1 , 1][down])) % loop
        tmp[out % key].append(pt[i])

        # turn the direction
        if i % (key - 1) == 0:
            down = not down

    tmp = sum(tmp , [])
    return tmp

def encrypt(ct , key):
    return "".join(rail_fence(ct , key))

# mapping the key locate by encryption
def decrypt(ct , key):
    rng = range(len(ct))
    index = rail_fence(rng , key)
    return "".join(ct[index.index(i)] for i in rng)

