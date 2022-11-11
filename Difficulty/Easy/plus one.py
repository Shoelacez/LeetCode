digits = [1, 2, 3]

'''APPROACH 01'''
# last_num = digits[len(digits) - 1]
# last_num += 1
#
# digits[len(digits) - 1] = last_num
#
# print(digits)

'''APPROACH 02'''
# 1. Construct an integer from the list
number = 0
for i in range(len(digits)):
    r = digits[i] * 10 ** (len(digits) - (1 + i))
    number += r

# print(number)

# 2. Increment the number by 1
number += 1
og_num = number

# 3. Reconstructing back the list
output = []
while number > 0:
    # print(number)
    rem = number % 10
    output.append(rem)
    number = number // 10



# 4. Reversing the number
correct_order = []
for i,n in enumerate(output):
    r = output[(len(output)-1)-i]
    correct_order.append(r)

print(correct_order)