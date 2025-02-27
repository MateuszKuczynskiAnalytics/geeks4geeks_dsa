n = 678

class Solution:
    def reverseDigits(self, n):
        digits = []
        while n != 0:
            digit = n % 10
            digits.append(digit)
            n = n // 10
        res = 0
        for i in range(len(digits)):
            res += digits[i] * 10 ** (len(digits) - (i + 1))
        return res 

obj = Solution()
ans = obj.reverseDigits(n)
print(ans) 
