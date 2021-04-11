class Solution:
    def isRectangleOverlap(self, rec1: 'List[int]', rec2: 'List[int]') -> 'bool':
        return min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]) > 0 and min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]) > 0


if __name__ == "__main__":
    print(Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
    print(Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))
