roman_numerals = dict([('I', 1), ('II', 2), ('III', 3), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
r_nums = dict(i=1, ii=2, iii=3, v=5, x=10, l=50, c=100, d=500, m=1000)

print(roman_numerals)

s = input("roman Number: ").upper()

chars = list(s)
print(chars)
# print(chars[0])

# Refernce point be the first char, is the next xhar ahead of it in the alphabet?
nine = 'ix'
# next is bigger so next - prev : 10 - 1

eleven = 'xi'
# next is smaller so next + prev : 10 + 1

# initializing the vars
prev_num = 0
next_num = 0

# print('III' in roman_numerals)
# print('IIII' in roman_numerals)

# print(roman_numerals[prev_num])

nums = list()

sum = 0

for items in chars:
    if items in roman_numerals:
        # print(roman_numerals[items])
        nums.append(roman_numerals[items])
    else:
        print("you are joking right?")
        break
        # if next_num > prev_num:
        #      # here we need the logic to subtract
        #      sum = next_num - prev_num
        # else:
        #     # result=next_num + prev_num
        #     sum += roman_numerals[items]

# print(f"{s}: {sum}")
# print(nums)


for num in range(len(nums)):
    print(num)
# if nums[ii] > nums[0]:
#     result = nums[1] - nums[0]
#     print(result)
#
# else:
#     result = nums[1] + nums[0]
#     print(result)

# print(f"Max of {nums[0]} and {nums[1]} : {max(nums)}")
