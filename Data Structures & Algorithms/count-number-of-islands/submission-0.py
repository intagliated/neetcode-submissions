class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c):
            if r<rows and c<cols and r>=0 and c>=0 and grid[r][c]== '1':
                grid[r][c]='0'
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
         

        import sys
        sys.setrecursionlimit(50000)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== '1':
                    count+=1
                    dfs(r,c)
        return count
                    
        

             
            


        
        