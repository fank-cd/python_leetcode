
# @Title: 按奇偶排序数组 II (Sort Array By Parity II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-12 12:10:28
# @Runtime: 212 ms
# @Memory: 15.7 MB

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        size = len(A)
        j = 0
        for i in range(1,size,2):
            if A[i] % 2 == 0:
                while A[j] %2 ==0:
                    j += 2
                A[i],A[j] = A[j],A[i]
        return A
