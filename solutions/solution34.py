class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while right > left:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        lower_bound = left

        left, right = 0, len(nums) - 1
        while right > left:
            mid = ((left + right) >> 1) + ((left + right) & 1)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        upper_bound = left
        return [lower_bound, upper_bound] if lower_bound <= upper_bound and nums[lower_bound] == target else [-1, -1]


if __name__ == '__main__':
    # print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    # print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
    print(Solution().searchRange([], 0))
