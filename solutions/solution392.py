class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        for ch in t:
            if s_pointer < len(s) and ch == s[s_pointer]:
                s_pointer += 1
        return s_pointer == len(s)


if __name__ == '__main__':
    print(Solution().isSubsequence(s="abc", t="ahbgdc"))
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))
