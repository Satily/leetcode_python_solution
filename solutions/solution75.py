class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l0, l1 = 0, 0
        for index in range(len(nums)):
            if nums[index] == 0:
                nums[index], nums[l0] = nums[l0], nums[index]
                if nums[index] == 1:
                    nums[index], nums[l0 + l1] = nums[l0 + l1], nums[index]
                l0 += 1
            elif nums[index] == 1:
                nums[index], nums[l0 + l1] = nums[l0 + l1], nums[index]
                l1 += 1


if __name__ == "__main__":
    nums = [1, 0]
    Solution().sortColors(nums)
    print(nums)
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
