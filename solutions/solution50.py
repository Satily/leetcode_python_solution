class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        result = 1.0
        if n < 0:
            n = -n
            x = 1 / x
        acc = x
        while n > 0:
            if n & 1 == 1:
                result *= acc
            n >>= 1
            if n == 0:
                break
            acc *= acc
        return result


if __name__ == "__main__":
    print(Solution().myPow(2.00000, 10))
    print(Solution().myPow(2.10000, 3))
    print(Solution().myPow(2.00000, -2))
    print(Solution().myPow(0.00000, -2))
    print(Solution().myPow(0.00000, 0))
