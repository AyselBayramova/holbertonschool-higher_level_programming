#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Xüsusi simvolları təyin edirik
    chars = [".", "?", ":"]
    
    i = 0
    # Mətnin əvvəlindəki boşluqları təmizləyirik
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            i += 1
            # Simvoldan sonra gələn bütün boşluqları keçirik (skip)
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
