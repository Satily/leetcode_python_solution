class BinaryExploder(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        num = self.num
        if num != 0:
            value, length = num & 1, 1
            num >>= 1
            while num != 0:
                if num & 1 != value:
                    yield value, length
                    value, length = num & 1, 0
                length += 1
                num >>= 1
            yield value, length


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ln = list(BinaryExploder(N))
        if len(ln) == 0:
            return 0
        if ln[0][0] == 0:
            ln = ln[1:]
        max_gap = 0
        if len(list(filter(lambda x: x[0] == 1 and x[1] > 1, ln))) > 0:
            max_gap = 1
        m = list(map(lambda x: x[1], filter(lambda x: x[0] == 0, ln)))
        if len(m) > 0:
            max_gap = max(max_gap, max(m) + 1)
        return max_gap


if __name__ == "__main__":
    print(Solution().binaryGap(22))
    print(Solution().binaryGap(5))
    print(Solution().binaryGap(6))
    print(Solution().binaryGap(1))
    print(Solution().binaryGap(8))
