a = 2
r = 2
n = 4

class Solution:
    def Nth_term(self, a, r, n):
        mod = 10**9 + 7
        return (a * pow(r, n - 1, mod)) % mod

obj = Solution()
ans = obj.Nth_term(a, r, n)