from functools import reduce


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        for num in nums:
            num_dict.setdefault(num, 0)
            num_dict[num] += 1
        n = self.factor(len(nums))
        for i in num_dict.values():
            n //= self.factor(i)
        result = []
        for _ in range(n):
            result.append(nums.copy())
            self.nextPermutation(nums)
        return result

    def factor(self, num):
        return reduce(lambda x, y: x * y, range(1, num + 1))

    def nextPermutation(self, nums):
        """
        Same as Solution 31
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        last = nums[ln - 1]
        index = ln - 2
        while nums[index] >= last and index >= 0:
            last = nums[index]
            index -= 1
        pivot_index = index
        # Find Pivot Ceil After Pivot
        if pivot_index >= 0:
            pivot_ceil_index = pivot_index + 1
            for index in range(pivot_index + 1, ln):
                if nums[pivot_index] < nums[index] <= nums[pivot_ceil_index]:
                    pivot_ceil_index = index
            # Swap to Pivot
            nums[pivot_ceil_index], nums[pivot_index] = nums[pivot_index], nums[pivot_ceil_index]
        # Reverse
        i = pivot_index + 1
        j = ln - 1
        while i < j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i += 1
            j -= 1


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
