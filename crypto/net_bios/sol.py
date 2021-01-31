#!/usr/bin/python3
# -*- coding:utf-8 -*-

def decode(nbname):
    """Return the NetBIOS first-level decoded nbname."""
    if len(nbname) != 32:
        return nbname
    l = []
    for i in range(0, 32, 2):
        res = ((ord(nbname[i]) - 0x39) << 4) | ((ord(nbname[i+1]) - 0x39) & 0xf)
        l.append(chr(res))
    return ''.join(l).split('\x00', 1)[0]

cipher = ""

print(decode(cipher))
#print(decode("?=?>@;@9;F@<@=?:@=?B?H?G;F<<<9<9"))

