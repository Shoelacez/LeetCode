a = "11"
b = "1"

a_copy = a


def bin_dec(bin_num):
    a = int(bin_num)
    count = 0
    while a >= 1:
        a /= 10
        count += 1

    number = 0
    for i in range(count):
        x = 2** i
        number += x
    return number


def add(num1,num2):
    n1 = bin_dec(num1)
    n2 = bin_dec(num2)

    total = n1+n2
    return total

print(add("11", "100"))

def dec_bin(num):
    bits = []
    while num != 0:
        rem = num % 2
        num = num  // 2
        bits.append(rem)
    return bits

bits = dec_bin(add("11", "1"))
print(bits)