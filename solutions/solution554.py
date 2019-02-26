class Solution:
    def leastBricks(self, wall: 'List[List[int]]') -> 'int':
        spaces = {}
        p = 0
        for level in wall:
            p = 0
            for brick in level:
                p += brick
                spaces.setdefault(p, 0)
                spaces[p] += 1
        spaces[p] = 0
        return len(wall) - max(spaces.values())


if __name__ == "__main__":
    print(Solution().leastBricks(
        [[1, 2, 2, 1],
         [3, 1, 2],
         [1, 3, 2],
         [2, 4],
         [3, 1, 2],
         [1, 3, 1, 1]]
    ))
    print(Solution().leastBricks(
        []
    ))
