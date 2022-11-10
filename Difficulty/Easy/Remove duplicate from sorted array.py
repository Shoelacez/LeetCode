nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k = 0
uniques = []
for n in nums:
    if n in uniques:
        pass
    else:
        k += 1
        uniques.append(n)

print(k)
print(uniques)
