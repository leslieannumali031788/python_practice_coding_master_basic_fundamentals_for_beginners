count = 0

for i in range(10):
    num = int(input("Enter number: "))
    if num % 2 != 0:
        count += 1

print("The number of odd numbers are:", count)