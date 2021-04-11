from itertools import accumulate


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sums = list(accumulate(nums))
        sums_map = {0: 1}
        result = 0
        for s in sums:
            d = s - k
            sums_map.setdefault(d, 0)
            result += sums_map.get(d)
            sums_map.setdefault(s, 0)
            sums_map[s] += 1

        return result


if __name__ == "__main__":
    # print(Solution().subarraySum([1], 0))
    # print(Solution().subarraySum([1, 1, 1], 2))
    # print(Solution().subarraySum([-1, -1, 1], 0))
    print(Solution().subarraySum([1, 1, 1], 2))
