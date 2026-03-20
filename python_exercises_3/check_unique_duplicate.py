# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
nums = []
duplicates = {}
while True:
    try:
        num = float(input("Enter number: "))
        nums.append(num)
        if num not in duplicates:
            duplicates[num] = 1
            print("Unique")
        else:
            duplicates[num] = duplicates[num] + 1
            print("Duplicate")
    except ValueError:
        break