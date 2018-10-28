class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_index = [(num, index) for index, num in enumerate(nums)]
        nums_with_index.sort(key=lambda item: item[0])
        left, right = 0, len(nums_with_index) - 1
        while left < right and nums_with_index[left][0] + nums_with_index[right][0] != target:
            if nums_with_index[left][0] + nums_with_index[right][0] < target:
                left += 1
            else:
                right -= 1
        return [nums_with_index[left][1], nums_with_index[right][1]]

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 3], 6))
