n = 3
a = 3
r = 2

class Solution:
    def sum_of_gp(self, n, a, r):
        if r == 1:
            return int(a * n)
        else:
            return int(a * (1 - pow(r, n)) / (1 - r))  


obj = Solution()
ans = obj.sum_of_gp(n, a, r)
print(ans)