# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
#create map of uppercase letters and use it as basis for the uppercase equivalent
#first came to mind but inefficient
# uppercase_list = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P",
#                 "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z"}
#use ord() then convert back using chr()

def upper(text: str) -> str:
    new_text = ""
    for char in text:
        if "a" <= char <= "z":
            new_text += chr(ord(char) - 32)
        else:
            new_text += char
    return new_text