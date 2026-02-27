from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        counting = 0
        
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    
                    if (0 <= new_r < rows and 
                        0 <= new_c < columns and 
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in visit):
                        
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    counting += 1
        
        return counting