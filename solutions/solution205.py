class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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
    print(Solution().isIsomorphic('egg', 'add'))
    print(Solution().isIsomorphic('foo', 'bar'))
    print(Solution().isIsomorphic('paper', 'title'))
