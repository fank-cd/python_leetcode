
# @Title: 有序数组的平方 (Squares of a Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2020-10-16 11:11:44
# @Runtime: 240 ms
# @Memory: 15.6 MB

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        size = len(A)
        res = [0 for _ in range(size)]
        
        left, right = 0, size - 1
        p = size - 1
        while left <= right:
            left_squre = A[left] * A[left]
            right_squre = A[right] * A[right]

            if left_squre > right_squre:
                res[p] =left_squre
                left += 1
            else:
                res[p] =right_squre
                right -= 1
            p -= 1
        
        return res



