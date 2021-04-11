from queue import Queue


class Solution:
    def shortestBridge(self, A: 'List[List[int]]') -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(A)
        n = len(A[0]) if m != 0 else 0

        q = Queue()
        q2 = Queue()      
        flag = False
        for x in range(m):
            for y in range(n): 
                if A[x][y] == 0:
                    A[x][y] = -2
                elif A[x][y] == 1 and not flag:
                    q.put((x, y))
                    q2.put((x, y))                    
                    A[x][y] = 0
                    flag = True
                    
        while not q.empty():
            cx, cy = q.get()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 1:
                    q.put((nx, ny))
                    q2.put((nx, ny))
                    A[nx][ny] = 0

        for x in range(m):
            for y in range(n):                
                if A[x][y] == 1:
                    A[x][y] = -1

        while not q2.empty():
            cx, cy = q2.get()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if A[nx][ny] == -2:
                        q2.put((nx, ny))
                        A[nx][ny] = A[cx][cy] + 1
                    elif A[nx][ny] == -1:
                        return A[cx][cy]
        return 0

if __name__ == "__main__":
    print(Solution().shortestBridge([[0,1],[1,0]]))
    print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
