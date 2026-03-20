# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
num_list = []
duplicates = []
for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    if num in num_list and num not in duplicates:
        duplicates.append(num)
    else:
        num_list.append(num)
print(duplicates)