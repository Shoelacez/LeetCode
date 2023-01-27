class Solution:
    # Coverting the binary number to a decimal number
    def bin_to_dec(self, bin_num):
        bin_num_og = bin_num
        bin_num = int(bin_num)
        count = 0
        decimalNum = 0
        while bin_num >= 1:
            rem = bin_num % 10
            decimalNum += rem * (2 ** count)
            count += 1
            bin_num = bin_num // 10

        return decimalNum

    def add_nums(self, num1, num2):
        n1 = self.bin_to_dec(num1)
        n2 = self.bin_to_dec(num2)
        return n1 + n2

    def dec_to_bin(self, result):
        bits = ""
        while result != 0:
            bit = result % 2
            bits += str(bit)
            result = result // 2

        else:
            bits = "0"
            return bits

        return bits

    def addBinary(self, a: str, b: str) -> str:
        # converting the binary num ->decimal
        # Adding the numbers
        result = self.add_nums(a, b)

        # Converting the dec num -> binary
        sum = self.dec_to_bin(result)
        return sum[::-1]

a="1010"
b="1011"
soln = Solution()
answer = soln.addBinary(a,b)
print(answer)
