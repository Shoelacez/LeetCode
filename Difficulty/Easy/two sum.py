nums = [3,3]
target = 6
expected_output = [0, 1]

for i in range(len(nums)):
    # print(f"Case: {nums[i]}")
    for j in range(i + 1, len(nums)):
        # print(nums[j])
        if nums[i] + nums[j] == target:
            print(f"{i, j}")
