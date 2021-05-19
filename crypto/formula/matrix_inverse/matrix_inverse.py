#!/usr/bin/python3

"""
https://math.stackexchange.com/questions/2686150/inverse-of-a-modular-matrix
"""

from string import printable
import gmpy2
import numpy as np

def list2arr(ls:list , row:int , col:int):
    return np.array(ls).reshape(row , col)

def arr2list(arr:np.ndarray):
    return arr.flatten().tolist()

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

def str_to_num(s:str,list , alpha:str):
    assert len(np.array(ls).shape) == 1 , "list should be 1-demensial"

    res = []
    for i in range(len(ls)):
        res.append(alpha.index(s[i]))

    return res

def matrix_inverse(arr:np.ndarray , mod:int):
    assert mod > 0 , "mod should greater than 0"

    adj = np.linalg.inv(arr).dot(np.linalg.det(arr))
    det = int(np.linalg.det(arr))

    try:
        inv = int(gmpy2.invert(det , mod))
    except:
        raise ZeroDivisionError("No inverse exist")

    res = np.mod(adj * inv , mod)
    res = np.round(res , 0).astype(int)

    return res.tolist()

if __name__ == "__main__" :
    alpha = printable[:62] + "_"    #default
    mod = len(alpha)
    ls = []
    row , col = 3 , 3               #default
    arr = list2arr(ls , row , col)
    arr , mod = input_process()

    print(matrix_inverse(arr))
