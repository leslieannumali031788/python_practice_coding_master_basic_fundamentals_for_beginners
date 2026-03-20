# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
def isupper(text: str) -> bool:
    for char in text:
        if char.isalpha() and char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  # remove uppercase characters list comprehension for simplicity
            return False
    return True
