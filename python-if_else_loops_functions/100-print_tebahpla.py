#!/usr/bin/python3

# Loop from ASCII 'z' (122) down to 'a' (97)
for char_code in range(122, 96, -1):
    # Use conditional expression within format:
    # If char_code is even, print it as is (lowercase).
    # If char_code is odd, subtract 32 to get uppercase ASCII.
    print("{}".format(chr(char_code if char_code % 2 == 0 else char_code - 32)), end="")
