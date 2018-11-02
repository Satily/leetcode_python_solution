class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        q = 0
        for p in range(0, len(nums)):
            if nums[p] != val:
                nums[q] = nums[p]
                q += 1
        return q


if __name__ == "__main__":
    input_list = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
    ]
    for input_line in input_list:
        nums = input_line[0].copy()
        val = input_line[1]
        result = Solution().removeElement(nums, val)
        print(nums, result)

