class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left, right = 0, 1
        s, r = nums[0], 0
        while (right != len(nums) or s >= k) and left != len(nums):
            if s == k:
                r += 1
                s -= nums[left]
                left += 1
            elif s > k or right == len(nums):
                s -= nums[left]
                left += 1
            else:
                s += nums[right]
                right += 1
        return r


if __name__ == "__main__":
    print(Solution().subarraySum([1], 0))
    print(Solution().subarraySum([1, 1, 1], 2))
