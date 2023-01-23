# link:
# https://leetcode.com/problems/search-insert-position/

nums = [1, 3, 5, 6]
target = 5
output = 2

for i in range(len(nums)):
    # print(nums[i])
    # target is in the list nums
    if nums[i] == target:
        print(i)
        break

    # target is not in the list nums
    # 1. Target fits in betwwen
    elif nums[i] > target:
        print(i)
        break

    else:
        print(len(nums))
        break

