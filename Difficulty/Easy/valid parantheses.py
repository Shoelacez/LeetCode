s = '(){}[]'
# s = '(){}(]'

p = {
    "(": ")",
    "[": "]",
    "{": "}",
}
valid = False
prev = []
for i,char in enumerate(s):
    # Even indices can not be values
    if i % 2 == 0:
        if s[i] not in p:
            valid = False
            break
        prev.append(s[i])

    # Odd indices should be values of keys s[i]
    else:
        if s[i] == p[prev[i//2]]:
            valid = True
        else:
            valid = False

if valid:
    print("Valid Parenthes")
else:
    print("Invalid Paranthesis")






