a1 = 2
a2 = 3
n = 4

a1 + (a2 - a1) * (n - 1)


class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        return a1 + (a2 - a1) * (n - 1)
