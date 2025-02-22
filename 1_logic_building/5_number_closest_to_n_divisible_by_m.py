from math import floor, sqrt
n = -13
m = 5

class Solution:
    def closestNumber(self, n , m):
        lower = floor(n / m) * m
        higher = floor((n / m) + 1) * m
        if abs(n - lower) == abs(n - higher):
            return lower if abs(lower) > abs(higher) else higher
        if abs(n - lower) < abs(n - higher):
            return lower
        else:
            return higher

obj = Solution()
ans = obj.closestNumber(n, m)