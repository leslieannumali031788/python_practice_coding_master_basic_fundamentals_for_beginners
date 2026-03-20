# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
#based on my other program

def endswith(text: str, suffix: str) -> bool:
    if text.find(suffix) == len(text) -len(suffix):
        return True
    return False
print(endswith("jehosh", "sh"))
#shorter version of the first function, less readable
def endswith(text: str, suffix: str) -> bool:
    return text.find(suffix) == len(text) - len(suffix)