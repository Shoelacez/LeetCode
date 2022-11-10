strs = ["flower", "flow", "flight"]

chars = []
for w in strs:
    print(f"for {w}")
    for c in w:
        print(c)
        chars.append(c)

print(chars)