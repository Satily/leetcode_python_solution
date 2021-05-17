class Solution:
    def minCut(self, s: str) -> int:
        s_len = len(s)
        is_palindrome = [[False] * (s_len + 1) for _ in range(s_len + 1)]

        for length in range(0, s_len + 1):
            for index in range(0, s_len - length + 1):
                if length <= 1 or is_palindrome[index + 1][length - 2] and s[index] == s[index + length - 1]:
                    is_palindrome[index][length] = True

        result = [s_len * 2] * (s_len + 1)
        result[0] = 0
        for index in range(0, s_len):
            for length in range(1, s_len - index + 1):
                if is_palindrome[index][length]:
                    result[index + length] = min(result[index + length], result[index] + 1)

        return result[s_len] - 1


if __name__ == '__main__':
    print(Solution().minCut("aab"))
    print(Solution().minCut("a"))
    print(Solution().minCut("ab"))
    print(Solution().minCut("aabcc"))
