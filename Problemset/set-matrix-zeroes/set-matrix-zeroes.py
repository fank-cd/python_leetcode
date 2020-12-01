
# @Title: 矩阵置零 (Set Matrix Zeroes)
# @Author: 2464512446@qq.com
# @Date: 2019-12-16 11:59:44
# @Runtime: 116 ms
# @Memory: 12.1 MB

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        pos = []

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    pos.append((i,j))

        for i,j in pos:
            self.heng(matrix,i,j,row,col)
            self.shu(matrix,i,j,row,col)

    def heng(self,matrix,i,j,row,col):
        x,y = i,0
        for _ in range(col):
            matrix[x][_] = 0

    def shu(self,matrix,i,j,row,col):
        x,y = 0,j
        for _ in range(row):
             matrix[_][y] = 0

