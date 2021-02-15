#!/usr/bin/python

text = open("output.txt",'r').read()#.decode('hex')
freq = sorted(set(text), key = text.count)[::-1]

englishLetterFreq = ' ETAOINSHRDLCUMWFGYPBVKJXQZ'

mapping = {}

for i , t in enumerate(freq):
    if i < 27:
        mapping[t] = englishLetterFreq[i]

res = ''
for c in text:
    if c in mapping.keys():
        res += mapping[c]

print(res)
