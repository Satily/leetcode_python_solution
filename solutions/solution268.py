class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        ln = len(nums)
        for index in range(ln):
            while ln > nums[index] != index:
                nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
        for index, num in enumerate(nums):
            if num == ln:
                return index
        return ln


if __name__ == "__main__":
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
