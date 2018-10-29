class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        abc_set = set()
        max_length = 0
        start_pos = 0
        for i, c in enumerate(s):
            while c in abc_set:
                abc_set.discard(s[start_pos])
                start_pos += 1
            abc_set.add(c)
            if i - start_pos + 1 > max_length:
                max_length = i - start_pos + 1
        return max_length


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))
    print(Solution().lengthOfLongestSubstring(''))
