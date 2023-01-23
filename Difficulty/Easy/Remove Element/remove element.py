nums = [3, 2, 2, 3, 5]
val = 3


counter = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[counter] = nums[i]
        counter += 1
        print(counter)

print(nums)

