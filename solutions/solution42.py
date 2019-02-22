class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        def fold_max(heights):
            max_height = heights[0]
            result = []
            for h in heights:
                max_height = max(max_height, h)
                result.append(max_height)
            return result

        if len(height) == 0:
            return 0
        left = fold_max(height)
        right = list(reversed(fold_max(list(reversed(height)))))

        return sum(map(lambda x: x[0] - x[1], zip(map(min, zip(left, right)), height)))


if __name__ == '__main__':
    print(Solution().trap([]))
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
