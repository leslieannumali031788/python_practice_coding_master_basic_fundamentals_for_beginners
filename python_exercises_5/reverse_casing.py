# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz
# almost same as prog05
name_list = []
name = input("Enter your name: ")
char_list = name.split()

for char in char_list:
    new_string = ""
    chars = list(char)

    for x in range(len(chars)):
        if "A" <= chars[x] <= "Z":
            new_string += chr(ord(chars[x]) + 32)
        else:
            new_string += chr(ord(chars[x]) - 32)
    name_list.append(new_string)

new_name = " ".join(name_list)
print(new_name)