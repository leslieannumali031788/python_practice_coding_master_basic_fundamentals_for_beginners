# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz
#used string slicing
def remove_space(text: str):
    for i in range(len(text)):
        if text[i] !=  " ":
            return text[i:]
print(remove_space("         Juan Dela Cruz"))