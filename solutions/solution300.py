class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        dp = []
        for num in nums:
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right + 1) >> 1
                if num < dp[mid]:
                    right = mid - 1
                elif num > dp[mid]:
                    left = mid + 1
                else:
                    left = mid
                    break
            if left == len(dp):
                dp.append(num)
            else:
                dp[left] = num
        return len(dp)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([2, 2]))
    print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
