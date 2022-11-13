list1 = [1, 2, 4]
list2 = [1, 3, 4]

expected_output = [1, 1, 2, 3, 4, 4]
output = []

for item1, item2 in zip(list1, list2):
    output.append(item1)
    output.append(item2)

print(output)
