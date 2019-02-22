class Solution:
    def findComplement(self, num: 'int') -> 'int':
        return int(''.join(map(str, map(lambda x: 1 - x, map(int, bin(num)[2:])))), 2)


if __name__ == "__main__":
    print(Solution().findComplement(5))
    print(Solution().findComplement(1))

