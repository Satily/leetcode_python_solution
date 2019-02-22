class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s, t = pattern, str.split(' ')
        if len(s) != len(t):
            return False
        d0, d1 = {}, {}
        for index in range(len(s)):
            d0.setdefault(s[index], t[index])
            if d0.get(s[index]) != t[index]:
                return False
            d1.setdefault(t[index], s[index])
            if d1.get(t[index]) != s[index]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat dog"))
    print(Solution().wordPattern("abba", "dog cat cat fish"))
    print(Solution().wordPattern("aaaa", "dog cat cat dog"))
    print(Solution().wordPattern("abba", "dog dog dog dog"))
