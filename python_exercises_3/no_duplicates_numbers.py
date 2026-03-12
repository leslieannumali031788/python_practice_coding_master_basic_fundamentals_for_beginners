number_list = []
for i in range(10):
    user_input = float(input("Enter a number:"))
    number_list.append(user_input)

print("These are the numbers that appeared only once:")
for listed_number in number_list:
    if number_list.count(listed_number) == 1:
        print(listed_number)
        
