from itertools import zip_longest


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = list(map(lambda x: sum(map(lambda y: int(y), x)), zip_longest(reversed(num1), reversed(num2), fillvalue='0')))
        c = 0
        for index in range(len(result)):
            result[index] += c
            result[index], c = result[index] % 10, result[index] // 10
        if c != 0:
            result.append(c)
        return ''.join(map(lambda x: str(x), reversed(result)))


if __name__ == "__main__":
    print(Solution().addStrings('342', '733'))
    print(Solution().addStrings('342', '1733'))
    print(Solution().addStrings('999', '1'))
