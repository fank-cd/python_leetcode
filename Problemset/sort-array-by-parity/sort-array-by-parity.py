
# @Title: 按奇偶排序数组 (Sort Array By Parity)
# @Author: 2464512446@qq.com
# @Date: 2019-10-08 17:17:35
# @Runtime: 72 ms
# @Memory: 12.1 MB

# class Solution(object):
#     def sortArrayByParity(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         i,j = 0,len(A)-1
#         while i<j:
#             if A[i] % 2 != 0:
#                 while A[j] %2 != 0 and j >i:
#                     j -=1
#                 A[i],A[j] = A[j], A[i]
#                 j -=1
#             i +=1

#         return A

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A
