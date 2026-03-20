# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
# same logic used from my other program
def swapcase(text: str) -> str:
    new_string = ""
    for char in text:
        chars = list(char)

        for x in range(len(chars)):
            if "A" <= chars[x] <= "Z":
                new_string += chr(ord(chars[x]) + 32)
            elif "a" <= chars[x] <= "z":
                new_string += chr(ord(chars[x]) - 32)
            else:
                new_string += chars[x]

    return new_string