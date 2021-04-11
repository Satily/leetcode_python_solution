class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max0 = max1 = max2 = -1001
        min0 = min1 = 1001
        for num in nums:
            if num > max0:
                max0, max1, max2 = num, max0, max1
            elif num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
            if num < min0:
                min0, min1 = num, min0
            elif num < min1:
                min1 = num
        return max(max0 * max1 * max2, min0 * min1 * max0)


if __name__ == "__main__":
    print(Solution().maximumProduct([1, 2, 3]))
    print(Solution().maximumProduct([1, 2, 3, 4]))
    print(Solution().maximumProduct([1, 2, -3, -4]))
    print(Solution().maximumProduct([1, 2, -3, 4]))
