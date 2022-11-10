'''Explanation
CASE 01
nums1 = [1,2]
nums2 = [3]
median = [1,'2',3]

CASE 02
nums1 = [1,2]
nums2 = [3,4]
median = [1,'((2+3)/2)',4]
'''

nums1 = [1,2,3]
nums2 = [4]

combined = nums1+nums2
if len(combined) % 2 == 0:
    mid_ind_val2 = len(combined)//2

    mid_val1 = combined[mid_ind_val2-1]
    mid_val2 = combined[mid_ind_val2]

    median = ((mid_val1+mid_val2)/2)
    print(f"Merged array: {combined} and the median is ({median})")

else:
    mid_index = len(combined)//2
    mid_num = combined[mid_index]
    print(mid_num)

