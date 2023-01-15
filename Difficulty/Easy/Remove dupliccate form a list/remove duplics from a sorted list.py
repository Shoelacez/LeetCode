nums = [1, 1, 2]
result = [1, 2]


# uniques =[]
# [uniques.append(number) for number in head if number not in uniques]
#
# count = 0
# for i in range(1, len(uniques)+1):
#     count = i
#
# print(count)
#
# print(uniques)


def removeDuplicates(list_nums):
    count = 0

    uniques = []
    for num in nums:
        if num not in uniques:
            uniques.append(num)
            count += 1
    # print(uniques)

    return count

k = removeDuplicates(nums)
print(k)