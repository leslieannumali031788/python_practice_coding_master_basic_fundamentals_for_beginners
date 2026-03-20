# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
nums = []
while True:
    try:
        num = float(input("Enter number: "))
        nums.append(num)
    except ValueError:
        break
print(f"Sorted: {sorted(nums)}")