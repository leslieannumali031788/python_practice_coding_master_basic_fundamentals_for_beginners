# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#return -1 if substring is not found
def rindex(text: str, substring: str) -> int:
    for i in range(len(text) - 1, -1, -1):
        if text[i:i+len(substring)] == substring:
            return i
    return -1
