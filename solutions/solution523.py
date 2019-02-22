class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = [0]
        s = 0
        for num in nums:
            s += num
            sums.append(s)
        for i in range(len(sums)):
            for j in range(i + 2, len(sums)):
                r = (sums[j] - sums[i])
                if k != 0 and r % k == 0 or k == 0 and r == 0:
                    return True
        return False


if __name__ == "__main__":
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(Solution().checkSubarraySum([23, 4, 2, 6, 7], 6))
    print(Solution().checkSubarraySum([0, 0], 0))
