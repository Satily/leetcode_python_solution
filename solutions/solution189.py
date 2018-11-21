class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        if ln != 0:
            nums[:] = [nums[i] for i in range(-(k % ln), ln - k % ln)]


if __name__ == "__main__":
    inputs_list = [
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([-1, -100, 3, 99], 2),
        ([], 2),
    ]
    for nums, k in inputs_list:
        Solution().rotate(nums, k)
        print(nums)

