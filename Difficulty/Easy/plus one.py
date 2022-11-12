class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:     
        # 1. Construct an integer from the list
        number = 0
        for i in range(len(digits)):
            r = digits[i] * 10 ** (len(digits) - (1 + i))
            number += r

        # 2. Increment the number by 1
        number += 1
        og_num = number

        # 3. Reconstructing back the list
        output = []
        while number > 0:
            rem = number % 10
            output.append(rem)
            number = number // 10

        # 4. Reversing the number
        correct_order = []
        for i,n in enumerate(output):
            r = output[(len(output)-1)-i]
            correct_order.append(r)

        return correct_order