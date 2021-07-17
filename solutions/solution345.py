class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        ns = [e for e in s]
        left, right = 0, len(s) - 1
        while right > left:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            ns[left], ns[right] = ns[right], ns[left]
            left += 1
            right -= 1
        return "".join(ns)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))
    print(Solution().reverseVowels("aA"))
