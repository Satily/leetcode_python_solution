class Bounder(object):
    def __init__(self, nums):
        self.nums = list(set(nums))
        self.nums.sort()
        # self.nums = {num: i for i, num in enumerate(t_nums)}

    def lower_bound(self, num):
        left, right = 0, len(self.nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if self.nums[mid] <= num:
                left = mid
            else:
                right = mid
        return left

    def upper_bound(self, num):
        left, right = 0, len(self.nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if self.nums[mid] <= num:
                left = mid
            else:
                right = mid
        return right

    def bound(self, left, right):
        return self.nums[self.lower_bound(left): self.upper_bound(right)]


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bounder = Bounder(nums)
        last_num_index = {}
        for index, num in enumerate(nums):
            b = bounder.bound(num - t, num + t)
            print(bounder.nums, num - t, num + t, b)
            for num_in_bound in b:
                if num_in_bound in last_num_index and index - last_num_index[num_in_bound] <= k:
                    return True
            last_num_index[num] = index
        return False


if __name__ == "__main__":
    # print(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    # print(Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    print(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
