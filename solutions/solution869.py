class NumberExploder(object):
    def __init__(self, num):
        self.num_count = [0] * 10
        while num > 0:
            self.num_count[num % 10] += 1
            num //= 10

    def __eq__(self, other):
        for index in range(10):
            if self.num_count[index] != other.num_count[index]:
                return False
        return True


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 0:
            return False
        if N == 1:
            return True
        ne = NumberExploder(N)
        n = 1
        for _ in range(31):
            n *= 2
            tne = NumberExploder(n)
            if ne == tne:
                return True
        return False


if __name__ == "__main__":
    print(Solution().reorderedPowerOf2(1))
    print(Solution().reorderedPowerOf2(10))
    print(Solution().reorderedPowerOf2(16))
    print(Solution().reorderedPowerOf2(24))
    print(Solution().reorderedPowerOf2(46))
