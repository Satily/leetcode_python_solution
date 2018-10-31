class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lead2 = set("0123456")
        ls = len(s)
        dp = [0] * (ls + 1)
        dp[0] = 1
        for i in range(0, ls):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if i + 1 < ls:
                if s[i] == '1' or s[i] == '2' and s[i + 1] in lead2:
                    dp[i + 2] += dp[i]
        return dp[ls]


if __name__ == "__main__":
    print(Solution().numDecodings('27'))
    print(Solution().numDecodings('12'))
    print(Solution().numDecodings('226'))
