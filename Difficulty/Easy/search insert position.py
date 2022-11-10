nums = [1, 3, 5, 6]
target = 7

def expected_position():
    for i in range(len(nums)):
        if nums[i] > target:
            print(i)
            break
        else:
            print(len(nums))
            break

output = 2
for i in range(len(nums)):
    if nums[i] == target:
        print(i)
    else:
        expected_position()
        break
