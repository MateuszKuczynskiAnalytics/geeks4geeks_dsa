n = 4

class Solution:
    def seriesSum(self, n: int) -> int:
        numbers_list = []
        for i in range(0, n):
            number = i + 1
            numbers_list.append(number)
        return sum(numbers_list)
    