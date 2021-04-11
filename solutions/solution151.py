class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(filter(lambda x: x != '', reversed(s.split(' '))))


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world!  "))
    print(Solution().reverseWords("a good   example"))