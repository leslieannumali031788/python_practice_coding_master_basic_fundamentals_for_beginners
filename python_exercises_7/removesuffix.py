#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
#need to remove a part of string if it matches at the end

def remove_suffix(string: str, suffix: str) -> str:
    if string.endswith(suffix):
        return string[:-len(suffix)] # if string ends with the suffix, use indexing to remove the suffix by getting the length of it
    return string #return string if it does not end with suffix