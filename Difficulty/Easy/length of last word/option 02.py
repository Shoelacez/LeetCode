class Solution:
       def lengthOfLastWord2(self, s: str) -> int:
            i,length = len(s)-1, 0

            while s[i] == " ":
                i -= 1
            
            while i >= 0 and s[i] != " ":
                length += 1
                i -= 1

            return length


s= "  fly me to  the  moon   "
soln = Solution()
count = soln.lengthOfLastWord2(s)
print(count)