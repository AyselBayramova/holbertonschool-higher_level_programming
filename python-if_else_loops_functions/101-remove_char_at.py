#!/usr/bin/python3

def remove_char_at(str, n):
    """Creates a copy of the string, removing the character at position n."""
    if n >= 0:
        # Concatenate string before n and string after n
        return (str[:n] + str[n + 1:])
    else:
        # If n is negative, return the original string
        return (str)
