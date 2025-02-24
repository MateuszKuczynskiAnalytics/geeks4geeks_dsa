from math import pi

r = 5

class Solution:
    def calculateArea(self, r):
        return round(pi * r * r, 5)

obj = Solution()
ans = obj.calculateArea(r)
print(ans)