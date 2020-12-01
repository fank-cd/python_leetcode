
# @Title: 搜索二维矩阵 (Search a 2D Matrix)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 16:43:33
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1
        while left <= right:
            mid = left + (right-left) // 2
            num = matrix[mid//n][mid%n]
            if num  < target:
                left  = mid + 1
            elif num > target:
                right = mid - 1
            else:
                return True

        return False
