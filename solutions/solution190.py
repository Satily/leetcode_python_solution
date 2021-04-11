class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(reversed(bin(n)[2:].rjust(32, '0'))), 2)


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
    print(Solution().reverseBits(4294967293))
