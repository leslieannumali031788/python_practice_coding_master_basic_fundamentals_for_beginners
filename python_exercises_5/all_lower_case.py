# Prog04: Create a program that ask the user to input their fullname. Print the input in all lower case.
# Example:
# Input: Juan Dela Cruz
# Output: juan dela cruz

string = input("Enter string: ")
new_text = ""
# reversed the logic from prog03
for char in string:
    if "A" <= char <= "Z":
        new_text += chr(ord(char) + 32)
    else:
        new_text += char

print(new_text)