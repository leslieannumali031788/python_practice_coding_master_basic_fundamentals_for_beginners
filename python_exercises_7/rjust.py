#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
#rjust() add space or specified chars at the beginning of the string and subtracts the length of the string from the number of chars needed to add
#use built in * operation for string and multiply the given value. default is whitespace

def rjust(string: str, count: int, value: str = " ") -> str:
    return (count - len(string)) * value + string