strs = ["flower", "flow", "flight"]

tracker = False

common_in_all = []
for i in range(len(strs)):
    print(f"Case: {strs[i]}")
    for j in range(len(strs[i])):
        char = strs[i][j]
        print(char)

