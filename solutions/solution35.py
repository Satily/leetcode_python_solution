class Solution:
    def searchInsert(self, nums: 'List[int]', target: int) -> int:
        left, right = 0, len(nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return left if target <= nums[left] else left + 1

if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 7))
    print(Solution().searchInsert([1,3,5,6], 0))

    