class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [[0, 0], [0, nums[0]]]
        for index, num in enumerate(nums):
            for is_rob in range(0, 2):
                if index != 0:
                    if is_rob == 1 and index == len(nums) - 1:
                        dp[is_rob].append(dp[is_rob][-1])
                    else:
                        dp[is_rob].append(max(dp[is_rob][-1], dp[is_rob][-2] + num))
        return max(dp[0][len(nums)], dp[1][len(nums)])


if __name__ == "__main__":
    print(Solution().rob([1]))
    print(Solution().rob([2, 3, 2]))
    print(Solution().rob([1, 2, 3, 1]))
