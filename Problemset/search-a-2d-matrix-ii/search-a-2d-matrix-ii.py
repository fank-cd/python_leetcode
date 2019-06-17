
# @Title: 搜索二维矩阵 II (Search a 2D Matrix II)
# @Author: 2464512446@qq.com
# @Date: 2019-03-18 11:30:44
# @Runtime: 100 ms
# @Memory: 14.8 MB

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
#         分治法。

#     左下角的元素是这一行中最小的元素，同时又是这一列中最大的元素。比较左下角元素和目标：
#         若左下角元素等于目标，则找到
#         若左下角元素大于目标，则目标不可能存在于当前矩阵的最后一行，问题规模可以减小为在去掉最后一行的子矩阵中寻找目标
#         若左下角元素小于目标，则目标不可能存在于当前矩阵的第一列，问题规模可以减小为在去掉第一列的子矩阵中寻找目标
#     若最后矩阵减小为空，则说明不存在

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        # M 行
        # N 列
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False
