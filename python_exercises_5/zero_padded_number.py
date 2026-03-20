# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
# Example:
# Input: 143
# Output: 000143

num = int(input("Enter a number: "))
zeroes = (6 - len(str(num))) * "0"
print(zeroes + str(num))