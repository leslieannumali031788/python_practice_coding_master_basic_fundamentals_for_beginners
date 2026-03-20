# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14
count = 0
words = input("Enter sentence: ")
for word in words:
    if word == " ":
        count += 1

if words == "":
    print(0)
else:
    print(count + 1)