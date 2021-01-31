#!/usr/bin/python3

def xor(a , b):
    assert type(a) == type(a) == str
    #assert len(a) == len(b)
    res = ""
    for i in range(len(b)):
        res += chr(ord(a[i]) ^ ord(b[i]))
    return res

#pt = input("The Plaintext : ")
ct = input("The CipherText : ")

try :
    a = fromhex(a)
    b = fromhex(b)
except:
    print("Input format Error")

while 1:
    key = input("Enter the Key : ")
    try:
        key = fromhex(key)
    except:
        print("Key format Error")
        continue
    print("Result is {0}".format(xor(key , ct)))    
    
