class Solution:
    def partition(self, s: str) -> 'List[List[str]]':
        s_len = len(s)
        is_palindrome = [[False] * (s_len + 1) for _ in range(s_len + 1)]

        for length in range(0, s_len + 1):
            for index in range(0, s_len - length + 1):
                if length <= 1 or is_palindrome[index + 1][length - 2] and s[index] == s[index + length - 1]:
                    is_palindrome[index][length] = True

        result = [[] for _ in range(s_len + 1)]
        result[0] = [[]]
        for index in range(0, s_len):
            for length in range(1, s_len - index + 1):
                if is_palindrome[index][length]:
                    substring = s[index: index + length]
                    for single in result[index]:
                        result[index + length].append(single + [substring])

        return result[s_len]


if __name__ == '__main__':
    print(Solution().partition("aab"))
    print(Solution().partition("a"))
    print(Solution().partition("aabcc"))
