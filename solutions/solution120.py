import sys


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for x in range(1, len(triangle)):
            for y in range(len(triangle[x])):
                m = sys.maxsize
                if y != 0:
                    m = min(m, triangle[x - 1][y - 1] + triangle[x][y])
                if y != len(triangle[x]) - 1:
                    m = min(m, triangle[x - 1][y] + triangle[x][y])
                triangle[x][y] = m
        return min(triangle[-1])


if __name__ == "__main__":
    print(Solution().minimumTotal(
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
    ))
