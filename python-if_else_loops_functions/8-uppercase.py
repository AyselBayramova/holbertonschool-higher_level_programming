def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for char in str:
        # Hərfin kodunu tapırıq
        temp_char = ord(char)
        # Əgər hərf kiçikdirsə (a-z), ondan 32 çıxırıq
        if temp_char >= 97 and temp_char <= 122:
            temp_char -= 32
        # Yeni simvolu (böyük və ya olduğu kimi) çap edirik
        print("{}".format(chr(temp_char)), end="")
    # Bütün mətndən sonra yeni sətirə keçirik
    print("")
