# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers_list = []

for count in range(10):
    user_input = float(input("Enter a number:"))
    if user_input not in numbers_list:
        numbers_list.append(user_input)

print("These are the list of numbers without any duplicates:", numbers_list)
