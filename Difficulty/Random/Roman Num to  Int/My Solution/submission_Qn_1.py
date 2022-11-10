roman_numerals = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

class Solution(object):
    def romanToInt(self, _s):
        s = _s
        chars = list(s)
        result = roman_numerals[chars[-1]]

        i = 1
        while i < len(s):
            if roman_numerals[chars[-i]] > roman_numerals[chars[-i - 1]]:
                result -= roman_numerals[chars[-i - 1]]
            else:
                result += roman_numerals[chars[-i - 1]]
            i += 1

        print(result)

    romanToInt("", "VV")

# Solution link
# https://dev.to/seanpgallivan/solution-roman-to-integer-567f

#making sure vv,ll do not give answers

