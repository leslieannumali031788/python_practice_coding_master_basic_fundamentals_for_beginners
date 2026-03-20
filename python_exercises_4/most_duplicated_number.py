# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

nums = []
occurence = {}
duplicates = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except ValueError:
        for i in range(len(nums)):
            if nums[i] not in occurence:
                occurence[nums[i]] = 1
            else:
                occurence[nums[i]] = occurence[nums[i]] + 1
        max_duplicate = max(occurence.values())
        duplicates.extend([key for key, value in occurence.items() if value == max_duplicate])
        break

print(f"Number/s with most duplicate is: {duplicates}")