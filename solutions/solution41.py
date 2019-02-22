class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            j = nums[i] - 1
            while 0 < nums[i] <= len(nums) and nums[i] != i + 1 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
