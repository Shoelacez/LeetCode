roman_numerals=dict([('I',1),('II',2),('III',3),('V', 5),('X',10),('L', 50),('C',100),('D', 500),('M', 1000)])
s=input("roman Number: ").upper()
chars = list(s)
nums = list()
sum = 0

for items in chars:
    if items in roman_numerals:
        nums.append(roman_numerals[items])

if nums[1] > nums[0]:
    result = nums[1] - nums[0]
    print(result)

