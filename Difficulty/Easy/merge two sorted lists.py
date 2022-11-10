list1 = [1, 2, 4]
list2 = [1, 3, 4]

expected_output = [1, 1, 2, 3, 4, 4]

output = []
for index, number in enumerate(list1):
    output.append(number)
    for i, n in enumerate(list2):
        if index == i:
            output.append(n)

print(output)
