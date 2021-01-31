#!/usr/bin/python2

from hashlib import *

# {'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'}

f = lambda x : <hash>(x).hexdigest()

res = ""
i = 0
while 1 :
    if f(str(i))[] == res:
        print str(i)
        break
    else:
        i += 1



