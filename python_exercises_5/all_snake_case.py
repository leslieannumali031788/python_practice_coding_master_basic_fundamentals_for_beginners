# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz
# almost same logic as prog09 and prog05
name_list = []
name = input("Enter your name: ")
char_list = name.split()

for chars in char_list:
    new_string = ""

    for x in range(len(chars)):
        if "A" <= chars[x] <= "Z":
            new_string += chr(ord(chars[x]) + 32)
        else:
            new_string += chars[x]
    name_list.append(new_string)

new_name = "_".join(name_list)  # instead of joining using whitespace, join without any space
print(new_name)