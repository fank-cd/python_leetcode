
# @Title: 二维数组中的查找 (二维数组中的查找 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 12:13:40
# @Runtime: 64 ms
# @Memory: 17.2 MB

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
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


