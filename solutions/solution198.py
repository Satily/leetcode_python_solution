class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0, nums[0]]
        for index, num in enumerate(nums):
            if index != 0:
                dp.append(max(dp[-1], dp[-2] + num))
        return dp[len(nums)]


if __name__ == "__main__":
    print(Solution().rob([]))
    print(Solution().rob([1]))
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 7, 9, 3, 1]))
