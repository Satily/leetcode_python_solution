class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rotten = []
        fresh_number = 0
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    rotten.append((x, y))
                elif grid[x][y] == 1:
                    fresh_number += 1

        time_passed = 0
        while len(rotten) != 0:
            time_passed += 1
            rotten_last_minute = rotten
            rotten = []
            for x, y in rotten_last_minute:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        rotten.append((nx, ny))
                        fresh_number -= 1

        return -1 if fresh_number > 0 else (time_passed - 1 if time_passed > 0 else 0)



if __name__ == "__main__":
    print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(Solution().orangesRotting([[0,2]]))