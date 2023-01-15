nums = [-1, 0, 1, 2, -1, -4]

for i, number in enumerate(nums):
    print(f"Case: {number}")
    for j, num in enumerate(nums[i + 1:]):
        print(f"Case {num}")
        for k, n in enumerate(nums[i + 2:]):
            print(f"{number, num, n}")
            if number + num + n == 0:
                print(f"{number, num, n} sums to 0")

print("I will be back stronger")