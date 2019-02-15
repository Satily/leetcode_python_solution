class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':
        ln = len(nums)
        if ln < 2:
            return 0
        nums.sort()
        return max([nums[i + 1] - nums[i] for i in range(ln - 1)])


if __name__ == "__main__":
    print(Solution().maximumGap([3, 6, 9, 1]))
    print(Solution().maximumGap([10]))
