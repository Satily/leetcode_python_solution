class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = len(s)
        dp = [[False] * (ls + 1) for _ in range(0, ls)]
        max_length = 1
        max_length_start_pos = 0
        for i in range(0, ls):
            dp[i][0] = True
            dp[i][1] = True
        for l in range(2, ls + 1):
            for i in range(0, ls + 1 - l):
                if s[i] == s[i + l - 1] and dp[i + 1][l - 2]:
                    dp[i][l] = True
                    max_length = l
                    max_length_start_pos = i
            if max_length < l - 1:
                break
        return s[max_length_start_pos: max_length_start_pos + max_length]


if __name__ == "__main__":
    # print(Solution().longestPalindrome('babad'))
    # print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('babadada'))
