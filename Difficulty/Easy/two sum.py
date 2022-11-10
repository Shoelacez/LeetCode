nums = [2,7,11,15]
target = 9

output2 = []
for i,n in enumerate(nums):
    for index,num in enumerate(nums):
        two_sum = n+num
        if two_sum == target:
            print(f"{n} and {num} add up to {target}")
            output2.append(i)
            output2.append(index)

uniques=[]
[uniques.append(item) for item in output2 if item not in uniques]
print(uniques)
