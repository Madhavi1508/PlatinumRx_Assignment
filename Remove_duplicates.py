def remove_duplicates(s):
    result = ""

    for char in s:
        if char not in result:
            result += char

    return result
s=input()
print(remove_duplicates(s))
