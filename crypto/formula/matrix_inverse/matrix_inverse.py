#!/usr/bin/python3

"""
https://math.stackexchange.com/questions/2686150/inverse-of-a-modular-matrix
"""

from string import printable
import numpy as np

def gcd(a:int , b:int):
    if(b == 0): return a
    else: return gcd(b , a % b)

def inverse(s , t):
    """
    The inverse of :data:`u` *mod* :data:`v`.
    """

    if(gcd(s , t) - 1):
        raise ZeroDivisionError

    s3, t3 = s , t
    s1, t1 = 1, 0
    while t3 > 0:
        q = s3 // t3
        s1, t1 = t1, s1 - t1 * q
        s3, t3 = t3, s3 - t3 * q
    while s1<0:
        s1 = s1 + t
    return s1

def list2arr(ls:list , row:int , col:int):
    return np.array(ls).reshape(row , col)

def input_process():
    """
    Use input to get array
    End with EOF
    """

    ls = []

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
        inv = int(inverse(det , mod)) # TODO change to other invert
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

def known_plain(pt:str , ct:str , alpha:str , key_len:int):
    assert len(pt) == len(ct) , "Error with different length"

    mod = len(alpha)
    pt = str_to_num(pt , alpha)
    ct = str_to_num(ct , alpha)

    ct = list2arr(ct , key_len , key_len)
    pt = list2arr(pt , key_len , key_len)
    p_inverse = matrix_inverse(pt , mod)
    key = ct.dot(p_inverse)

    return key
    
if __name__ == "__main__" :
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!"
    c1 = "X.LEGIVPJ"
    p1 = "I_HATE_TO"
    c2 = "DBWCFIBWF"

    key = known_plain(p1 , c1 , alpha , 3).flatten().tolist()

    print(hill_decrypt(key , c2 , alpha))

