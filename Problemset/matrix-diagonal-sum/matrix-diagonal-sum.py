
# @Title: 矩阵对角线元素的和 (Matrix Diagonal Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-09-05 22:58:30
# @Runtime: 32 ms
# @Memory: 12.5 MB

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row_len = len(mat)
        col_len = len(mat[0])
        left_up = (0,0)
        right_up = (0,col_len-1)
        left_down = (row_len-1,0)
        right_down = (row_len-1,col_len-1)
        
        res = 0
        visited =set()
        row,col = left_up
        while True:
            
            if (row,col) not in visited:
                res += mat[row][col]
            visited.add((row,col))
            if (row,col) == right_down:
                break
            row += 1
            col += 1
        row,col = right_up
        while True:
            if (row,col) not in visited:
                res += mat[row][col]
            if (row,col) == left_down:
                break
            visited.add((row,col))
            row += 1
            col -= 1
        return res
