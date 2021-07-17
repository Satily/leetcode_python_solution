# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

bad = 4


def isBadVersion(version):
    return version >= bad


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while right - left > 0:
            mid = (left + right) >> 1
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    bad = 4
    print(Solution().firstBadVersion(5))
    bad = 1
    print(Solution().firstBadVersion(1))
