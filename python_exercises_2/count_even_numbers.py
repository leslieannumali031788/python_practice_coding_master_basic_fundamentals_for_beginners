evenNumbers = 0

for i in range(10):
    if int(input("Enter a number:")) % 2 == 0:
        evenNumbers += 1

print("There are", evenNumbers, "even numbers.")