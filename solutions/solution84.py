class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [(0, -1)]
        heights.append(0)
        result = 0
        for index, height in enumerate(heights):
            while height < stack[len(stack) - 1][0]:
                result = max(result, stack[len(stack) - 1][0] * (index - stack[len(stack) - 2][1] - 1))
                stack.pop()
            if height >= stack[len(stack) - 1][0]:
                stack.append((height, index))
        return result


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(Solution().largestRectangleArea([1, 4, 5, 4, 5, 4, 1]))
    print(Solution().largestRectangleArea([2, 1, 2]))
    print(Solution().largestRectangleArea([0, 9]))
