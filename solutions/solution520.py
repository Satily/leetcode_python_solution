class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def is_upper_case(ch):
            return 'A' <= ch <= 'Z'
        uppercase_count = sum(map(is_upper_case, word))
        return uppercase_count == 0 or uppercase_count == 1 and is_upper_case(word[0]) or uppercase_count == len(word)


if __name__ == "__main__":
    print(Solution().detectCapitalUse("USA"))
    print(Solution().detectCapitalUse("FlaG"))
