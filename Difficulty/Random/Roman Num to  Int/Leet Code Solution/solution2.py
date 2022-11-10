
roman_numerals = dict([('I', 1), ('II', 2), ('III', 3), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
sum = 0
curr = 0
prev = 0

s = input("s = ").upper()

for i in range(len(s)):
    curr = roman_numerals[s[i]]
    if curr > prev:
        sum = sum + curr - 2 * prev
    else:
        sum += curr
        prev = curr

print(sum)


