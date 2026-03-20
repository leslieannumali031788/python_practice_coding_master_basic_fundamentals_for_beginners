# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
# zfill() also ignores + or - at beginning and is placed after it

# longer version from short function
def zfill(text: str, width: int) -> str:
    if len(text) >= width:
        return text

    if text[0] in ("+", "-"):
        return f"{text[0]}{(width - len(text) + 1) * '0'}{text[1:]}"
    return f"{(width - len(text)) * '0'}{text}"


# short but sacrifice readability
# checks first if text starts with + or - using list indexing then skips it. if not, returns width * "0" + text
def zfill(text: str, width: int) -> str:
    if len(text) >= width:
        return text
    return f"{text[0]}{(width - len(text) + 1) * '0'}{text[1:]}" if text[0] in ("+",
                                                                                "-") else f"{(width - len(text)) * '0'}{text}"