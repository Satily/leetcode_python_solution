class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_num_index = {}
        for index, num in enumerate(nums):
            if num in last_num_index and index - last_num_index[num] <= k:
                return True
            last_num_index[num] = index
        return False


if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
