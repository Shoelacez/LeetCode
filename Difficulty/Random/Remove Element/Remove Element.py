# author @shoelacez
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
expected_output = [0, 1, 3, 0, 4]

for num in nums[:]:
    if val == num:
        nums.remove(num)

print(f'Here is the output: {nums}')
