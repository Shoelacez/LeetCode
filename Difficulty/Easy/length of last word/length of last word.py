class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start, end = 0,0 

        last_word = ''
        for i in range(len(s)):
            if s[i].isspace():
                start = i+1
                # print(f"Char at i = {i}: is a space")
            else:
                end = i
                # print(f"Start: {start}, End: {end}")
                last_word = s[start:end+1]
        print(last_word)