nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_output = [0, 1, 2, 3, 4]
number_of_uniques = 5

uniques = []
count = 0
for n in nums:
    if n not in uniques:
        uniques.append(n)
        count += 1

print(uniques)
print(f"There are {count} unique values")
