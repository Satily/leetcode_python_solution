class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        for ia, a in enumerate(map(int, reversed(num1))):
            for ib, b in enumerate(map(int, reversed(num2))):
                result[ia + ib] += a * b
        for index in range(len(result) - 1):
            result[index + 1] += result[index] // 10
            result[index] %= 10
        for index in reversed(range(1, len(result))):
            if result[index] == 0:
                result.pop()
            else:
                break
        return ''.join((map(str, reversed(result))))



if __name__ == '__main__':
    print(Solution().multiply('0', '0'))
    print(Solution().multiply('2', '3'))
    print(Solution().multiply('123', '456'))
