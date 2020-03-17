
# @Title: 有序矩阵中第K小的元素 (Kth Smallest Element in a Sorted Matrix)
# @Author: 2464512446@qq.com
# @Date: 2019-12-16 11:43:01
# @Runtime: 196 ms
# @Memory: 17.2 MB

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None
        row = len(matrix)
        col = row
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left+right) >> 1 # 位运算比除法快
          # mid = (left+right) /2
            count  = self.find(matrix,mid,row,col)
            if count < k:
                left = mid +1
            else:
                right = mid
        
        return right

        
    def find(self,matrix,mid,row,col):
        count  = 0
        i,j= row-1,0
        while(i >= 0 and j < col):
            if matrix[i][j] <= mid:
                count += i+1
                j += 1
            else:
                i -= 1

        return count

