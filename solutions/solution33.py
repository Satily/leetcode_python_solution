class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        left, right = 0, len(nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[left] and nums[mid] <= target < nums[left] or nums[left] <= nums[mid] and (nums[mid] <= target or target < nums[left]):
                left = mid
            else:
                right = mid
        if len(nums) != 0 and nums[left] == target:
            return left
        else:
            return -1



if __name__ == "__main__":
    # print(Solution().search([], 5))
    print(Solution().search([1, 3], 3))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
