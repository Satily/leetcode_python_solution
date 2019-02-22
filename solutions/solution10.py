class Character(object):
    def __init__(self, character, number):
        self.character = character
        self.number = number


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lp, ls = len(p), len(s)
        index = 0
        patten = []
        while index < lp:
            character = p[index]
            if index + 1 < lp and p[index + 1] == "*":
                number = 0
                index += 1
            else:
                number = 1
            patten.append(Character(character, number))
            index += 1
        lp = len(patten)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[0][0] = True
        for index_s in range(ls + 1):
            for index_p in range(lp):
                if dp[index_s][index_p]:
                    if index_s < ls and (patten[index_p].character == '.' or patten[index_p].character == s[index_s]):
                        dp[index_s + 1][index_p + 1] = True
                        if patten[index_p].number == 0:
                            dp[index_s + 1][index_p] = True
                    if patten[index_p].number == 0:
                        dp[index_s][index_p + 1] = True
        return dp[ls][lp]


if __name__ == "__main__":
    print(Solution().isMatch('a', 'ab*'))
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('ab', '.*'))
    print(Solution().isMatch('aab', 'c*a*b'))
    print(Solution().isMatch('mississippi', 'mis*is*p*.'))
