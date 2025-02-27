n = 687

class Solution:
    def sumOfDigits (self, n):
        n_str = str(n)
        numbers = [int(n_str[i]) for i in range(len(n_str))]
        result = sum(numbers)
        return result

obj = Solution()
ans = obj.sumOfDigits(n)
print(ans)