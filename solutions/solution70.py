class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
