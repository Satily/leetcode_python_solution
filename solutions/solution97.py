class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)
        if ls1 + ls2 != ls3:
            return False
        dp = [[False] * (ls2 + 1) for _ in range(0, ls1 + 1)]
        dp[0][0] = True
        for is1 in range(0, ls1 + 1):
            for is2 in range(0, ls2 + 1):
                if dp[is1][is2]:
                    if is1 < ls1 and s1[is1] == s3[is1 + is2]:
                        dp[is1 + 1][is2] = True
                    if is2 < ls2 and s2[is2] == s3[is1 + is2]:
                        dp[is1][is2 + 1] = True
        return dp[ls1][ls2]


if __name__ == "__main__":
    print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
