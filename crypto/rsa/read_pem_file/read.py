#!/usr/bin/python3

from Crypto.PublicKey.RSA import importKey

f = input("Input the file name : ")

f = importKey(open(f , "r").read())

print(f"n = {f.n}")
try:
    print(f"d = {f.d}")
    print(f"e = {f.e}")
except:
    print(f"e = {f.e}")


