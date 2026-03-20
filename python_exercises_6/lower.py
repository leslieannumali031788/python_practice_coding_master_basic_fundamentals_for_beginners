# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
def lower(text: str) -> str:
    new_text = ""
    for char in text:
        if "A" <= char <= "Z":
            new_text += chr(ord(char) + 32)
        else:
            new_text += char
    return new_text