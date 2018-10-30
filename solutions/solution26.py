class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        if ln == 0:
            return 0
        result = 1
        last = nums[0]
        for i in range(1, ln):
            if nums[i] != last:
                last = nums[i]
                result += 1
        return result


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
