# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.


def title(text: str) -> str:
    name_list = []
    char_list = text.split()

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

    return " ".join(name_list)