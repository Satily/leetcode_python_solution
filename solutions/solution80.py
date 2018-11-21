class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        p, q = 0, 0
        for i in range(1, len(nums)):
            if p == q and nums[i] == nums[p]:
                p += 1
                nums[p] = nums[i]
            elif nums[i] != nums[p]:
                p += 1
                q = p
                nums[p] = nums[i]
        pop_len = len(nums) - p - 1
        for _ in range(0, pop_len):
            nums.pop()
        return p + 1


if __name__ == "__main__":
    nums_list = [
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [],
        [1],
        [1, 2],
    ]
    for line in nums_list:
        nums = line.copy()
        result = Solution().removeDuplicates(nums)
        print(nums, result)