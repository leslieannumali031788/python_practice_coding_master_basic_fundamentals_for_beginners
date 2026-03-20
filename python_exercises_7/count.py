#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

#works but slow
def count(text: str, substring: str) -> int:
    found = []
    index = 0
    for _ in range(len(text)):
        string = text.find(substring, index)
        if string != -1:
            found += [string]
            index += 1
    return len(set(found))

#try to create more efficient algorithm
def count(text: str, substring: str) -> int:
    count = 0
    len_substring = len(substring)
    for i in range(len(text)):
        if text[i : i + len_substring] == substring:
            count += 1
    return count