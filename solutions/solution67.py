from itertools import zip_longest


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = list(map(sum, zip_longest(map(int, reversed(a)), map(int, reversed(b)), fillvalue=0)))
        for index in range(len(result) - 1):
            result[index + 1] += result[index] >> 1
            result[index] &= 1
        if result[-1] > 1:
            result[-1] &= 1
            result.append(1)
        return ''.join((map(str, reversed(result))))


if __name__ == '__main__':
    print(Solution().addBinary('11', '1'))
    print(Solution().addBinary('1010', '1011'))
