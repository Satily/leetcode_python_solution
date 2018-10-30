class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        # init
        dp = [[False] * (lp + 1) for _ in range(0, ls + 1)]
        for i in range(0, ls + 1):
            pass
        for i in range(0, lp + 1):
            pass
        dp[0][0] = True
        for pi in range(1, lp + 1):
            for si in range(1, ls + 1):
                if pi != 0 or si != 0:
                    if p[pi - 1] == '.' and dp[si - 1][pi - 1]:
                        dp[si][pi] = True
                    elif p[pi - 1] == '*' and (dp[si - 1][pi - 1] or dp[si - 1][pi]):
                        dp[si][pi] = True
                    elif p[pi - 1] == s[si - 1] and dp[si - 1][pi - 1]:
                        dp[si][pi] = True
        return dp[ls][lp]


if __name__ == "__main__":
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('ab', '.*'))
    print(Solution().isMatch('aab', 'c*a*b'))
    print(Solution().isMatch('mississippi', 'mis*is*p*.'))
