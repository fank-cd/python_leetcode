
# @Title: 旋转图像 (Rotate Image)
# @Author: 2464512446@qq.com
# @Date: 2018-11-07 14:44:25
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
                for j in range(i+1,length):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

