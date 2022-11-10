s = input("String: ")

uniques = []
for char in s:
    if char in uniques:
        pass
    else:
        uniques.append(char)

final_string = ''.join(uniques)

print(f"{final_string}, length: {len(final_string)}")