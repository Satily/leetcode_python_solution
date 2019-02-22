from itertools import groupby


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def index_of(nl):
            result = {}
            for index, num in enumerate(nl):
                result.setdefault(num, index)
            return result

        counts = {key: len(list(items)) for key, items in groupby(sorted(nums), lambda x: x)}
        max_count = max(counts.values())
        max_count_indices = set()
        for k, v in counts.items():
            if v == max_count:
                max_count_indices.add(k)

        left, right = {}, {}
        for index in range(len(nums)):
            left.setdefault(nums[index], index)
            right.setdefault(nums[len(nums) - 1 - index], len(nums) - 1 - index)
        lengths = {key: right[key] - value + 1 for key, value in left.items()}

        return min([lengths[index] for index in max_count_indices])



if __name__ == "__main__":
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
