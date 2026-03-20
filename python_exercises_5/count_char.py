# Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
# Example:
# Input: Juan Dela Cruz
# Output: 14
#same logic as prog07 but this time count all chars

string = input("Enter input: ")
count = len([x for x in string])
print(count)