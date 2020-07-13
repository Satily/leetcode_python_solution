class Solution:
    def titleToNumber(self, s: str) -> int:        
        result = 0
        for ch in s:
            result = result * 26 + ord(ch) - 64
        return result


if __name__ == "__main__":
    print(Solution().titleToNumber("A"))
    print(Solution().titleToNumber("AB"))
    print(Solution().titleToNumber("ZY"))
    print(Solution().titleToNumber("ZZ"))
    print(Solution().titleToNumber("AAA"))
    print(Solution().titleToNumber("AAZ"))
    print(Solution().titleToNumber("ABA"))