roman_numerals = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

r_num = "MCMXCIV"
chars = list(r_num)
result= roman_numerals[chars[-1]]

# for i in range(len(r_num)):
#     # print(chars[i])
#     '''Printing the characters backwards '''
#
#     # print(chars[len(r_num)-(i+1)])
#
#     if roman_numerals[chars[len(r_num)- (i+2)]] > roman_numerals[chars[len(r_num)- (i+1)]]:
#         result -= roman_numerals[chars[len(r_num)-(i+1)]]
#     else:
#         result += roman_numerals[chars[len(r_num)-(i+1)]]
#
# print(result)

i= 1

while i < len(r_num):
    if roman_numerals[chars[-i]] > roman_numerals[chars[-i-1]]:
        result -= roman_numerals[chars[-i-1]]
        # print(result)
    else:
        result += roman_numerals[chars[-i-1]]
        # print(result)

    i+=1

print(result)




