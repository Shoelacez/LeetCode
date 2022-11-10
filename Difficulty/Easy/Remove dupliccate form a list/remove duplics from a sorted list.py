head = [1, 1, 2, 3, 3]
result = [1, 2]

uniques =[]
[uniques.append(number) for number in head if number not in uniques]

print(uniques)