strs = ["flower", "flow", "flight"]
output = "fl"


x = [item for item in zip(strs[0], strs[1], strs[2])]
# print(x)

# Determinant is the shortest word
for word in strs:
    current = len(word)
    for item in range(1,len(strs)):
        if len(strs[item]) < current:
            shortest = len(strs[item]);
            print(shortest)
    break
