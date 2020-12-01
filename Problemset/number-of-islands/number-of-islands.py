
# @Title: 岛屿数量 (Number of Islands)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 15:59:33
# @Runtime: 84 ms
# @Memory: 14.1 MB

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        count = 0
        def helper(x,y):
            if 0 <= x < len(grid) and 0<= y < len(grid[0]) and grid[x][y] == "1":
                grid[x][y] = "0"
                helper(x+1,y)
                helper(x-1,y)
                helper(x,y+1)
                helper(x,y-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    helper(i,j)
        return count
