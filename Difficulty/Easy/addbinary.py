a = "1010"
b = "1011"


def convert_to_dec(binary):
    decimal_num = 0
    for i, char in enumerate(binary):
        digit = int(char)
        r = digit * 2 ** ((len(binary) - 1) - i)
        decimal_num += r
    return decimal_num


dec_a = convert_to_dec(a)
dec_b = convert_to_dec(b)

add_dec = dec_b + dec_a
add_bin = bin(add_dec)
print(add_bin[2:])
