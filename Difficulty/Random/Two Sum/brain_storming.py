'''Round 01'''
# nums = [2,7,11,15]
# target = 9
#
# in_nums = []
# for index, num in enumerate(nums):
#     # print(index, num)
#     # print(target-num)
#     result = target - num
#     if result in nums:
#         #instead of appending result we append that particular index
#         in_nums.append(index)
#         print(f"{num} is in nums")
#
# print(in_nums)

'''Round 02'''
# nums = [3, 2, 4]
# target = 6
#
# in_nums = []
# sum = 0
# for index, num in enumerate(nums):
#     # print(index, num)
#     # print(target-num)
#     result = target - num
#     if result in nums:
#         #instead of appending result we append that particular index
#         in_nums.append(index)
#         print(f"{num} is in nums")
#         #we need to add the contents linked to those indices
#         sum += nums[index]
#         #but we need only to the sum two values to get the target
#
#
#
# print(in_nums)
# print(sum)

'''Round 03'''
nums = [2, 7, 9, 15]
target = 9

result = nums[len(nums)-1]
print("The last element is: "+str(result))

in_nums=[]
i = 1
while i < len(nums):
    r = nums[len(nums)-i] + nums[len(nums)-i-1]
    if r == target:
        in_nums.append(nums[len(nums)-i])
        in_nums.append(nums[len(nums)-i-1])
    i+=1
    # print(i)

print(in_nums)

'''Round 04'''
# nums = [3, 1, 3]
# target = 6
#
# in_nums=[]
# i = 1
# j= 1
#
# while i < len(nums):
#     while j < len(nums):
#         r = nums[len(nums) - i] + nums[len(nums) - j - 1]
#         if r == target:
#             in_nums.append(nums[len(nums) - i])
#             in_nums.append(nums[len(nums) - j - 1])
#         # print(r)
#         j+=1
#     # r = nums[len(nums)-i] + nums[len(nums)-i-1]
#     # if r == target:
#     #     in_nums.append(nums[len(nums)-i])
#     #     in_nums.append(nums[len(nums)-i-1])
#     i+=1
#     # print(i)
#
# print(in_nums)

'''Round 05'''
# nums = [3, 1, 3]
# target = 6
#
# in_nums=[]
# i = 1
# j= 1
#
# while i < len(nums):
#     while j < len(nums):
#         r = nums[len(nums) - i] + nums[len(nums) - j - 1]
#         if r == target:
#             in_nums.append(nums[len(nums) - i])
#             in_nums.append(nums[len(nums) - j - 1])
#         # print(r)
#         j+=1
#     # r = nums[len(nums)-i] + nums[len(nums)-i-1]
#     # if r == target:
#     #     in_nums.append(nums[len(nums)-i])
#     #     in_nums.append(nums[len(nums)-i-1])
#     i+=1
#     # print(i)
#
# print(in_nums)


