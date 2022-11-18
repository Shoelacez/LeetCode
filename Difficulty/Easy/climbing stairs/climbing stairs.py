class Solution:
    def climbStairs(self, n: int) -> int:
        step_01,step_02 = 1, 1

        for i in range(n-1):
            t = step_01
            step_01 += step_02
            step_02 = t
        return step_01