class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)
        dp = [[False] * (ls2 + 1) for _ in range(0, ls1 + 1)]
        dp[0][0] = True
        for is1 in range(0, ls1):
            for is2 in range(0, ls2):
                pass


if __name__ == "__main__":
    print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
