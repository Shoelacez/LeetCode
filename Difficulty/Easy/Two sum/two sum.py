'''Approach o1'''
# nums = [3,3]
# target = 6
# expected_output = [0, 1]
#
# for i in range(len(nums)):
#     # print(f"Case: {nums[i]}")
#     for j in range(i + 1, len(nums)):
#         # print(nums[j])
#         if nums[i] + nums[j] == target:
#             print(f"{i, j}")

'''Approach 02'''
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#

'''APPROACH 03'''
nums = [3, 3]
target = 6
expected_output = [0, 1]

values = {}

for i, value in enumerate(nums):
    if target - value in values:
        print(f"{values[target-value],i}")
    else:
        values[value] = i
        print(f"{values[value]}")
