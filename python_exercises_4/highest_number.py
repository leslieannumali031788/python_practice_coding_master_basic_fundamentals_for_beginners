# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
nums = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except ValueError:
        break

print(max(nums))