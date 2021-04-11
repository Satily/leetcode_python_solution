class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A) - min(A) - K * 2, 0)


if __name__ == "__main__":
    print(Solution().smallestRangeI([1], 0))
    print(Solution().smallestRangeI([0, 10], 2))
    print(Solution().smallestRangeI([1, 3, 6], 3))
