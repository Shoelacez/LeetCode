strs = ["flower", "flow", "flight"]


result = zip(strs[0], strs[1], strs[2])

output = []
for item in result:
    print(item)
    if item[0] == item[1] == item[2]:
        output.append(item[0])


print("".join(output))

for item in strs:
    print(item)
    output.append(zip(item))


print(output)
for item in output:
    print(item)