class RangeParser(object):
    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        if len(self.nums) == 0:
            return
        left = right = self.nums[0]
        for num in self.nums[1:]:
            if num == right + 1:
                right = num
            else:
                yield left, right
                left = right = num
        yield left, right


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        for left, right in RangeParser(nums):
            if left == right:
                result.append(str(left))
            else:
                result.append(str(left) + '->' + str(right))
        return result


if __name__ == "__main__":
    print(Solution().summaryRanges([]))
    print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
    print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
