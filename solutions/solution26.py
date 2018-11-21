class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        q = 0
        for p in range(0, len(nums)):
            if nums[p] != nums[q]:
                q += 1
                nums[q] = nums[p]
        pop_len = len(nums) - q - 1
        for _ in range(0, pop_len):
            nums.pop()
        return q + 1


if __name__ == "__main__":
    nums_list = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [],
    ]
    for line in nums_list:
        nums = line.copy()
        result = Solution().removeDuplicates(nums)
        print(nums, result)
