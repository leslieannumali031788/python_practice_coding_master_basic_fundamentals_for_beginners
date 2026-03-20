# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
nums = []
while True:
    try:
        num = float(input("Enter number: "))
        nums.append(num)
    except ValueError:
        break
print(f"The lowest number is: {min(nums)}")