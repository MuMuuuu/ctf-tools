#!/usr/bin/python3
from string import ascii_lowercase

inp = input("Input the data like this x-xxx-xx-xxxx-xx-x : \n").strip().split("-")
alpha = list("_" + ascii_lowercase + "_")
nums = "1 2 22 222 3 33 333 4 44 444 5 55 555 6 66 666 7 77 777 7777 8 88 888 9 99 999 9999 0".split(" ")
dic = dict(zip(nums , alpha))

res = ""

for i in range(len(inp)):
    try:    
        inp[i] = dic[inp[i]]
    except KeyError:
        inp[i] = "?"

res = "".join(inp)
print(res)
