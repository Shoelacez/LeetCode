num = int(input("number: "))
was_neg = False
# Changing -ve nums to +ve
if num<0:
    num = -1 * num
    was_neg  = True
else:
    pass

counter = 0

numbers = []
while num != 0:
    # print(num)
    rem = num % 10
    print(rem)
    numbers.append(rem)
    num = num // 10
    counter += 1

print(numbers)

total = 0
for round in range(1, counter + 1):
    p = numbers[-round] * 10 ** (round - 1)
    total += p

if was_neg:
    total = -1 * total
else:
    pass

reversed_num = total
print(f"Reversed number: {reversed_num}")
