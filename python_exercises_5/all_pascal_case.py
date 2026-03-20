# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz
# same logic as prog05, slight tweak

name_list = []
name = input("Enter your name: ")
char_list = name.split()

for chars in char_list:
    new_string = ""

    if "a" <= chars[0] <= "z":
        new_string += chr(ord(chars[0]) - 32)
    else:
        new_string += chars[0]

    for x in range(1, len(chars)):
        if "A" <= chars[x] <= "Z":
            new_string += chr(ord(chars[x]) + 32)
        else:
            new_string += chars[x]
    name_list.append(new_string)

new_name = "".join(name_list)  # instead of joining using whitespace, join without any space
print(new_name)