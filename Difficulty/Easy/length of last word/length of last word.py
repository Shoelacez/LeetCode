class Solution:
    def lengthOfLastWord(self, s: str) -> int:
                s = s.lower()
                for i in range(len(s)):
                    if not s[i].islower():
                        last_word = s[i+1:]
                        
                for i in range(1, len(last_word)+1):
                    pass
                return i

s = "   fly me   to   the moon  "
soln = Solution()
result = soln.lengthOfLastWord(s)
print(result)