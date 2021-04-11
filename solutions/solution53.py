class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        result = max(nums)
        s = 0
        for num in nums:
            s += num
            result = max(result, s)
            if s < 0:
                s = 0
        return result


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
