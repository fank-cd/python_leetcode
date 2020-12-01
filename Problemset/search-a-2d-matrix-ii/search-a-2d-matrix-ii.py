
# @Title: 搜索二维矩阵 II (Search a 2D Matrix II)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 12:14:32
# @Runtime: 44 ms
# @Memory: 17.7 MB

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        

        if not matrix:
            return False

        if not isinstance(matrix,list) or not isinstance(matrix[0],list):
            return False

        if not isinstance(target,int):
            return False

        n = len(matrix)
        m = len(matrix[0])
        x,y = m-1,0


        while y < n and x >=0:
            # print(matrix[y][x],target)
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                return True

        return False


