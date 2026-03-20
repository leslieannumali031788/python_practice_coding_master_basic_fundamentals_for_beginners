# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
# rstrip() removes last character in argument list. skips if not included
# chars default is whitespace like in rstrip

def rstrip(text: str, chars: str = " ") -> str:
    # convert string to list
    text_list = [x for x in text]
    char_list = [x for x in chars]
    while True:
        if text_list[-1] in char_list:
            text_list.pop(-1)
        else:
            break
    return "".join(text_list)
