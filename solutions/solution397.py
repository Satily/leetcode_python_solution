class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 1:
            result += 1
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
            else:
                n += 1
        return result


# 1 11 +1/2/2/2 -1/2-1/2
# 1 10 /2-1
# 1 01 -1/2/2
# 1 00 /2/2

# 0011010010 -> /
# 01 -1/2/2
# 011 +1/2/2
# 0111
# 01111


#11111111


if __name__ == "__main__":
    print(Solution().integerReplacement(8))
    print(Solution().integerReplacement(7))
    print(Solution().integerReplacement(1234))
