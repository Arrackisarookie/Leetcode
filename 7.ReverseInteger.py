class Solution:
    # def reverse(self, x: int) -> int:
    #     sign = 1 if x > 0 else -1
    #     res = int(str(abs(x))[::-1])
    #     return sign * res if res < 2147483648 else 0

    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        rvs = 0
        x = abs(x)
        while x:
            rvs = rvs * 10 + x % 10
            x //= 10
        return sign * rvs if rvs < 2147483648 else 0
