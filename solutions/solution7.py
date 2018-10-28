class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2147483647
        min_int = -2147483648
        x2 = abs(x)
        flag = x > 0
        result = 0
        while x2 > 0:
            result = result * 10 + x2 % 10
            x2 = x2 // 10
        if not flag:
            result = -result
        if result > max_int or result < min_int:
            return 0
        return result


if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse((2 ** 30) * -2))
    print(Solution().reverse((2 ** 30 - 1) * 2 + 1))
