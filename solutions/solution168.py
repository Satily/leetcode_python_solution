class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''        
        while n != 0:
            n -= 1
            result = chr(65 + n % 26) + result
            n //= 26
        return result

if __name__ == "__main__":
    print(Solution().convertToTitle(1))
    print(Solution().convertToTitle(25))
    print(Solution().convertToTitle(26))
    print(Solution().convertToTitle(27))
    print(Solution().convertToTitle(28))
    print(Solution().convertToTitle(701))
    print(Solution().convertToTitle(702))
    print(Solution().convertToTitle(703))
    print(Solution().convertToTitle(704))
