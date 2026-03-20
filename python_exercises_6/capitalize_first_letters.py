# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
def capitalize(text: str) -> str:
    new_string = ""

    if "a" <= text[0] <= "z":
        new_string += chr(ord(text[0]) - 32)
    else:
        new_string += text[0]

    for x in range(1, len(text)):
        if "A" <= text[x] <= "Z":
            new_string += chr(ord(text[x]) + 32)
        else:
            new_string += text[x]

    return new_string