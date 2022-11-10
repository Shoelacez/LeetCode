x = -121
original_x = x
output = True

# split the number into individual nums
indiv_nums = []
digit_count = -1
while x > 0:
    rem = x % 10
    indiv_nums.append(rem)
    x = x // 10
    digit_count += 1

print(indiv_nums)

# Reverse the numbers
iteration = 0
length = len(indiv_nums)

reversed_number = 0
while iteration != length:
    reversed_number += indiv_nums[iteration] * 10 ** digit_count
    iteration += 1
    digit_count -= 1

print(reversed_number)

# Compare the reversed number to x, if same: True else False
if reversed_number == original_x:
    print("True")
else:
    print("False")
