# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

def center(text: str, width: int, char: str = " ") -> str:
    if len(text) >= width:
        return text

    required = width - len(text)
    left = required // 2
    right = required - left
    return f"{left * char}{text}{right * char}"