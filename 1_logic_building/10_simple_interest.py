p = 100
r = 20
t = 2

class Solution:
    def simpleInterest(self,A,B,C):
        return ((B/100) * A) * C

obj = Solution()
ans = obj.simpleInterest(p, r, t)
print(ans)