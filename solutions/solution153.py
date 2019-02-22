class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        left, right = 0, len(nums)
        if right == 0:
            return -1
        result = nums[0]
        while left + 1 < right:
            mid = (left + right) >> 1
            result = min(result, nums[mid])
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
        return min(result, nums[left])


if __name__ == "__main__":
    print(Solution().findMin([3, 4, 5, 1, 2]))
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
