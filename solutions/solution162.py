class Solution:
    def findPeakElement(self, nums: 'List[int]') -> int:
        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = (left + right) >> 1
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
        return left if nums[left] > nums[right] else right
        


if __name__ == "__main__":
    print(Solution().findPeakElement([1,2,3,1]))
    print(Solution().findPeakElement([1,2,1,3,5,6,4]))
