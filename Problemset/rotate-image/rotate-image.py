
# @Title: 旋转图像 (Rotate Image)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 18:16:30
# @Runtime: 24 ms
# @Memory: 11.5 MB

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # for i in range(len(matrix)):
        #     for j in range(i, len(matrix[0])):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # 转置和水平翻转两个步骤。

        # for row in matrix:
        #     row.reverse()
        matrix[:] = map(list,zip(*matrix[::-1]))
