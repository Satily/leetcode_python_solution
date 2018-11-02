class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_map = {num: index for index, num in enumerate(nums1)}
        stack = [-1]
        result = {}
        for num in reversed(nums2):
            while len(stack) != 0 and stack[-1] <= num:
                stack.pop()
            if num in nums1_map:
                if len(stack) == 0:
                    result[nums1_map[num]] = -1
                else:
                    result[nums1_map[num]] = stack[-1]
            stack.append(num)
        return [result[index] for index in sorted(result.keys())]


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
