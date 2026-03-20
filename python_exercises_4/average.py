# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
nums = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except ValueError:
        break

print(f"Average: {sum(nums) / len(nums)}")