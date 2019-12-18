from itertools import zip_longest


from queue import Queue


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m = len(grid)
        n = len(grid[0]) if m != 0 else 0        
        result = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    q = Queue()
                    q.put((x, y))
                    while not q.empty():
                        cx, cy = q.get()
                        grid[cx][cy] = 2
                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '2'
                                q.put((nx, ny))
                    result += 1
        return result


   
def grouper(iterable, n, fillvalue=None):
    n = len(iterable) // n
    args = [iter(iterable)] * n
    return list(map(lambda x: list(x), zip_longest(*args, fillvalue=fillvalue)))

if __name__ == "__main__":
    print(Solution().numIslands(grouper('11110110101100000000', 4)))
    print(Solution().numIslands(grouper('11000110000010000011', 4)))
    