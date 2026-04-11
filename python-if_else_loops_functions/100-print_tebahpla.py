#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        char_code = i
    else:
        char_code = i - 32
    print("{}".format(chr(char_code)), end="")
