class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        last = nums[ln - 1]
        index = ln - 2
        while nums[index] >= last and index >= 0:
            last = nums[index]
            index -= 1
        pivot_index = index
        # Find Pivot Ceil After Pivot
        if pivot_index >= 0:
            pivot_ceil_index = pivot_index + 1
            for index in range(pivot_index + 1, ln):
                if nums[pivot_index] < nums[index] <= nums[pivot_ceil_index]:
                    pivot_ceil_index = index
            # Swap to Pivot
            t = nums[pivot_ceil_index]
            nums[pivot_ceil_index] = nums[pivot_index]
            nums[pivot_index] = t
        # Reverse
        i = pivot_index + 1
        j = ln - 1
        while i < j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i += 1
            j -= 1


if __name__ == "__main__":
    nums_list = [
        # [1, 2, 3],
        # [3, 2, 1],
        # [1, 1, 5],
        # [1],
        # [1, 1],
        [2, 3, 1, 3, 3],
    ]
    for nums in nums_list:
        nums2 = nums.copy()
        for _ in range(0, 6):
            Solution().nextPermutation(nums2)
            print(nums2)
