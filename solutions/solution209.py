import sys


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sn = 0
        left, right = 0, 0
        result = sys.maxsize
        while len(nums) > right:
            s -= nums[right]
            right += 1
            while s <= 0:
                result = min(result, right - left)
                s += nums[left]
                left += 1
        if result == sys.maxsize:
            return 0
        else:
            return result


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
