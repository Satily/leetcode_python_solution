class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        q = 0
        for p in range(0, len(nums)):
            if nums[p] != 0:
                nums[p], nums[q] = nums[q], nums[p]
                q += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
