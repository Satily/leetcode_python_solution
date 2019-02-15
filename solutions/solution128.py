class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        nums2 = sorted(set(nums))
        start, res = 0, 0
        for i in range(1, len(nums2)):
            if nums2[i] != nums2[i - 1] + 1:
                start, res = i, max(res, i - start)
        res = max(res, len(nums2) - start)
        return res


if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
