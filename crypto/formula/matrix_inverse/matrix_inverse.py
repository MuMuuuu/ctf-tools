#!/usr/bin/python3

"""
https://math.stackexchange.com/questions/2686150/inverse-of-a-modular-matrix
"""

from string import printable
import gmpy2
import numpy as np

def list2arr(ls:list , row:int , col:int):
    return np.array(ls).reshape(row , col)

def input_process():
    ls = []

    print("Input the array , end with Ctrl-d or empty newline")
    while(True):
        try:
            ls.append(list(map(int , input().strip().split(" "))))
        except:
            break

    arr = np.array(ls).astype(int)

    try:
        mod = int(input("mod : "))
    except:
        quit()

    return arr , mod

def num_to_str(ls:list , alpha:str):
    assert len(np.array(ls).shape) == 1 , "list should be 1-demensial"

    res = []
    for i in range(len(ls)):
        res.append(alpha[ls[i]])

    return res

def str_to_num(s:str , alpha:str):
    assert len(np.array(list(s)).shape) == 1 , "list should be 1-demensial"

    res = []
    for i in range(len(s)):
        res.append(alpha.index(s[i]))

    return res

def matrix_inverse(arr:np.ndarray , mod:int):
    assert mod > 0 , "mod should greater than 0"

    adj = np.linalg.inv(arr).dot(np.linalg.det(arr))
    det = int(np.linalg.det(arr))

    col , row = arr.shape # only square matrix is invertable

    try:
        inv = int(gmpy2.invert(det , mod))
    except:
        raise ZeroDivisionError("No inverse exist")

    res = np.mod(adj * inv , mod)
    res = np.round(res , 0).astype(int)
    res = res.reshape(col , row)
    
    return res

def hill_decrypt(key:list , cipher:str , alpha=printable[:62]+"_"):
    mod = len(alpha)
    row = col = int(pow(len(key) , 0.5))

    key = list2arr(key , row , col)
    key = matrix_inverse(key , mod)

    cipher = str_to_num(cipher , alpha)
    cipher = list2arr(cipher , row , len(cipher) // row)

    res = key.dot(cipher) % mod
    plaint = num_to_str(res.flatten().tolist() , alpha)

    return "".join(plaint)

if __name__ == "__main__" :
    # Test data
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!"
    cipher = "_VGUPIMW!S_TBBS"
    key = [21 , 11 , 10,  27,  6 , 16 , 15 , 9 , 5]

    print(hill_decrypt(key , cipher , alpha))

