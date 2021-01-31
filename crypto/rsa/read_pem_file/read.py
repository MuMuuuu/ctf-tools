#!/usr/bin/python3

from Crypto.PublicKey.RSA import importKey

f = input("Input the file name : ")

f = importKey(open(f , "r").read())

print(f.n)
print(f.e)
