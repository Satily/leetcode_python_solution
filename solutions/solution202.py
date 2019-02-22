class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tried = set()
        while n not in tried and n != 1:
            tried.add(n)
            n2 = 0
            while n > 0:
                n2, n = n2 + (n % 10) ** 2, n // 10
            n = n2
        return n == 1


if __name__ == "__main__":
    print(Solution().isHappy(19))