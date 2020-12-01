
# @Title: 岛屿的周长 (Island Perimeter)
# @Author: 2464512446@qq.com
# @Date: 2020-10-30 10:34:20
# @Runtime: 304 ms
# @Memory: 13.7 MB

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x_len,y_len = len(grid),len(grid[0])
        count = 0
        def helper(x,y):
            nonlocal count
            dire = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in dire:
                new_x,new_y=  x + i, y + j
                # print(new_x,new_y)
                if new_x < 0 or new_x >= x_len :
                    count += 1
                if new_y < 0 or new_y >= y_len :
                    count += 1
                elif  0<= new_x < x_len and 0<= new_y < y_len and grid[new_x][new_y] == 0:
                    count += 1
        
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == 1:
                    helper(i, j)
        return count

