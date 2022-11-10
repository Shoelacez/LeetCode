nums = [3,2,2,3]
val = 3

k = 2
expected_nums = [2,2]
nums.sort()

iterations = len(nums)
print(nums)
for i in range(iterations):
    if val == nums[i]:
        nums.pop(i)
        break



print(nums)