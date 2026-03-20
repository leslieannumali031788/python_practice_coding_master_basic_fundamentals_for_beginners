#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#use .find() since it returns the index of the first occurence and if it returns 0, it starts with that, else False if it returns -1
#long version, morpe readable
def startswith(text: str, prefix: str) -> bool:
    if text.find(prefix) == 0:
        return True
    return False

#shorter version of the first function, less readable
def startswith(text: str, prefix: str) -> bool:
    return text.find(prefix) == 0