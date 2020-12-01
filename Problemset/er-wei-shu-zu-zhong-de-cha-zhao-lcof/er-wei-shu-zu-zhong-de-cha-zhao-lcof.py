
# @Title: 二维数组中的查找 (二维数组中的查找 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-04-20 12:14:03
# @Runtime: 20 ms
# @Memory: 16.2 MB

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows=len(matrix)
        row,col = 0,len(matrix[0])-1

        while row < rows and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True
        return False
rix[y][x] < target:
                y += 1
            else:
                return True

        return False


