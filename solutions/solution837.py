class Solution:
    def new21Game(self, N: 'int', K: 'int', W: 'int') -> 'float':
        if K == 0:
            return 1.0
        dp = [[0] * (N + 1) for _ in range(2)]
        dp[0][0] = 1
        p = 1 / W
        c, n = 1, 0
        result = 0
        for i in range(K):
            c, n = n, c
            dp[n] = [0] * (N + 1)
            for j in range(i, K):
                for k in range(W):
                    o = j + k + 1
                    if o > N:
                        break
                    dp[n][o] += dp[c][j] * p
            result += sum(dp[n][K:])
        return result


if __name__ == "__main__":
    print(Solution().new21Game(0, 0, 1))
    print(Solution().new21Game(10, 1, 10))
    print(Solution().new21Game(6, 1, 10))
    print(Solution().new21Game(21, 17, 10))
