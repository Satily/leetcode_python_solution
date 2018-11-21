class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 1:
            return 0

        height_positions = [(h, i) for i, h in enumerate(height)]
        height_positions.sort(reverse=True)
        result = 0
        left = right = height_positions[0][1]
        for i in range(1, len(height_positions)):
            left = min(left, height_positions[i][1])
            right = max(right, height_positions[i][1])
            result = max(result, height_positions[i][0] * (right - left))
        return result


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
