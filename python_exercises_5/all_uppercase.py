# Prog03: Create a program that ask the user to input their fullname. Print the input in all capital letter.
# Example:
# Input: Juan Dela Cruz
# Output: JUAN DELA CRUZ

string = input("Enter string: ")
new_text = ""
# same logic as upper() function i made
for char in string:
    if "a" <= char <= "z":
        new_text += chr(ord(char) - 32)
    else:
        new_text += char

print(new_text)