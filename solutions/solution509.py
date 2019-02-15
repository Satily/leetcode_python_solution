class Solution:
    def fib(self, N: 'int') -> 'int':
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))