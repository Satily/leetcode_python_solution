class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(0, len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:i + len(word)] == word:
                        dp[i + len(word)] = True
        return dp[len(s)]


if __name__ == "__main__":
    print(Solution().wordBreak('leetcode', ["leet", "code"]))
    print(Solution().wordBreak('applepenapple', ["apple", "pen"]))
    print(Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))