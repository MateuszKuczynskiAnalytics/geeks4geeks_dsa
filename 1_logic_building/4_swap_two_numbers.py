a, b = 5, 8

class Solution:
    def get(self, a, b):
        b, a = a, b
        return a, b

obj = Solution()
ans = obj.get(a, b)