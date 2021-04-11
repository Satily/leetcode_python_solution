class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2         
        p = 1
        while n > 4:
            n -= 3
            p *= 3
        return p * n


if __name__ == "__main__":
    print(Solution().integerBreak(2))
    print(Solution().integerBreak(3))
    print(Solution().integerBreak(4))
    print(Solution().integerBreak(5))
    print(Solution().integerBreak(6))
    print(Solution().integerBreak(7))
    print(Solution().integerBreak(8))
    print(Solution().integerBreak(9))
    print(Solution().integerBreak(10))