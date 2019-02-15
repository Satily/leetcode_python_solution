class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        ls, lp = len(s), len(p)
        if p == '*' or ls == 0 and lp == 0:
            return True
        elif ls == 0 or lp == 0:
            return False
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[0][0] = True
        for pi in range(1, lp + 1):
            if p[pi - 1] == '*':
                dp[0][pi] = True
            else:
                break
        for pi in range(1, lp + 1):
            for si in range(1, ls + 1):
                if p[pi - 1] == '*':
                    dp[si][pi] = dp[si][pi - 1] or dp[si - 1][pi - 1] or dp[si - 1][pi]
                elif p[pi - 1] == '?' or p[pi - 1] == s[si - 1]:
                    dp[si][pi] = dp[si - 1][pi - 1]
        return dp[ls][lp]


if __name__ == "__main__":
    # Solution().isMatch("", "")
    # Solution().isMatch("", "*")
    # Solution().isMatch("", "**")
    # Solution().isMatch("", "*?")
    # Solution().isMatch("", "?*")
    # Solution().isMatch("a", "*")
    # Solution().isMatch("a", "**")
    # Solution().isMatch("a", "*?")
    # Solution().isMatch("a", "?*")
    # Solution().isMatch("aa", "")

    print(Solution().isMatch("", "?"))
    print(Solution().isMatch("b", "??"))
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa", "*"))
    print(Solution().isMatch("cb", "?a"))
    print(Solution().isMatch("adceb", "*a*b"))
    print(Solution().isMatch("acdcb", "a*c?b"))
