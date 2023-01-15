strs = ["flower", "flow", "flight"]
output = "fl"


# def longestCommonPrefix(words):
#     res = ""
#     for i in range(len(strs[0])):
#         for s in strs:
#             if i == len(s) or s[i] != strs[0][i]:
#                 return res
#         res += strs[0][i]
#     return res
#
#
# answer = longestCommonPrefix(strs)
# print(answer)


def longestCommonPrefix(words):
    res = ""
    for i in range(len(strs[0])):
        print(f"i: {i}")
        for s in strs:
            print(s)
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


answer = longestCommonPrefix(strs)
print(answer)