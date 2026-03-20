# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
def lstrip(text: str, chars: str = " ") -> str:
    # convert string to list
    text_list = [x for x in text]
    char_list = [x for x in chars]
    while True:
        if text_list[0] in char_list:
            text_list.pop(0)
        else:
            break
    return "".join(text_list)
