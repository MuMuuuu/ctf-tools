#!/usr/bin/python

from subprocess import check_output

newmap={
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "\n",   #Enter
41: "esc",
42: "del",
43: "   ",  #tab
44: " ",    #space
45: "-",
47: "[",
48: "]",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}

name = raw_input("Input pcap file : ").strip()
inp = check_output(["tshark" , "-r" , name , "-T" , "fields" , "-e" , "usb.capdata"]).strip().replace(":" , "").replace("\n" , "")
inp_ls = [inp[i : i + 16] for i in range(0 , len(inp) , 16)]

flag = ""

for line in inp_ls:
    dec = line.strip().replace("00" , "").decode("hex")

    try:
        val = ord(dec[-1])
    except:
        continue

    if val in newmap:
        now = newmap[val]
        if now != "PostFail":
            flag += now
        elif now == "del":
            del flag[-1]
    else:
        print("Unexpect val : {}".format(val))

print(flag)

