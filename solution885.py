class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> 'List[List[int]]':
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        uncolored = R * C       
        result = []
        x, y = r0, c0
        turns = 0        
        while uncolored > 0:
            dx, dy = directions[turns % 4]
            step = (turns // 2) + 1
            for _ in range(step):
                if 0 <= x < R and 0 <= y < C:
                    uncolored -= 1
                    result.append([x, y])                    
                x, y = x + dx, y + dy
            turns += 1
        return result

if __name__ == "__main__":
    print(Solution().spiralMatrixIII(1, 4, 0, 0))
    print(Solution().spiralMatrixIII(5, 6, 1, 4))