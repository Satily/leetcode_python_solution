class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)


if __name__ == "__main__":
    print(Solution().minMoves([1, 2, 3]))
