'''CORRECT SOLUTION'''
'''MY OWN SOLUTION THAT WAS WRONG'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        for x, h in enumerate(height):
            for _x, _h in enumerate(height):
                # Calculate the area btn them
                if height[x] < height[_x]:
                    smallest = height[x]
                else:
                    smallest = height[_x]

                l = abs((x - _x))
                area = l* smallest
                # print(area)
                areas.append(area)

        uniques = []
        for a in areas:
            if a not in uniques:
                uniques.append(a)

        return max(uniques)