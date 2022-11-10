s = "Hello World"
output = 5

for i,char in enumerate(s):
    if str.isspace(char):
        last_word = s[i:]

print(last_word)

