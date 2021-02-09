#!/usr/bin/python2

from hashlib import *

# {'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'}
h = ""

f = exec("lambda x : {}(x).hexdigest()".format(h))

res = ""
i = 0
while 1 :
    # [ ] input which section you need
    if f(str(i))[] == res:
        print str(i)
        break
    else:
        i += 1

