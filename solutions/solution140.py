class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ls = len(s)
        dp = [[] for _ in range(ls + 1)]
        dp[0] = [0]
        for i in range(0, ls):
            if dp[i]:
                for word in wordDict:
                    if s[i:i + len(word)] == word:
                        dp[i + len(word)].append(i)
        memories = [[] for _ in range(ls + 1)]
        memories[ls] = ['']
        for i in reversed(range(1, len(s) + 1)):
            for forward in dp[i]:
                memories[forward].extend(map(lambda x: s[forward:i] + " " + x, memories[i]))
        return list(map(lambda x: x.rstrip(), memories[0]))


if __name__ == "__main__":
    print(Solution().wordBreak("a", []))
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
