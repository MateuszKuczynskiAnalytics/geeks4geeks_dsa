n = 5

class Solution:
    def oppositeFaceOfDice(self, n):
        dice = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
        return dice.get(n)


obj = Solution()
ans = obj.oppositeFaceOfDice(n)