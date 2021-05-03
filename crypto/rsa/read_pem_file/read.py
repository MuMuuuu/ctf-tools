#!/usr/bin/python3

from Crypto.PublicKey.RSA import importKey
from glob import glob
from sys import argv 

if len(argv) == 1:
    print("Usage : ./read.py <file> <file> ...")
    exit()

for i in argv[1:]:
    for j in glob(i):
        f = importKey(open(j , "r").read())

        print("=" * 5 + " {} ".format(j) + "=" * 5)
        print(f"n = {f.n}")
        try:
            print(f"d = {f.d}")
            print(f"e = {f.e}")
        except:
            print(f"e = {f.e}")


