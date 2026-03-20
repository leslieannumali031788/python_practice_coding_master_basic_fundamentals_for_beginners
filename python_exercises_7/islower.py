# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
# use lowercase list
def islower(text: str) -> bool:
    for char in text:
        if char.isalpha() and char not in 'abcdefghijklmnopqrstuvwxyz':  # remove lowercase characters list comprehension for simplicity
            return False
    return True


# revised version, more readable and faster
def islower(text: str) -> bool:
    for char in text:
        if char.isalpha() and not "a" <= char <= "z":  # remove lowercase characters list comprehension for simplicity
            return False
    return True
