nums = [0,1,2,2,3,0,4,2]
val = 2
expected_output = 2
# nums = [2, 2, 0, 0]

result = []
count = 0
for num in nums:
    if val != num:
        result.append(num)
        count += 1
    
print(result)
print(count)