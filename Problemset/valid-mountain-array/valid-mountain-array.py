
# @Title: 有效的山脉数组 (Valid Mountain Array)
# @Author: 2464512446@qq.com
# @Date: 2020-11-03 12:35:31
# @Runtime: 236 ms
# @Memory: 14.9 MB

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        left,right = 0 ,len(A)-1
        if len(A) <3:
            return False
        while left < len(A)-1:
            if A[left] < A[left+1]:
                left += 1
            else:
                break
        while right >= 0:
            if A[right] < A[right-1]:
                right -= 1
            else:
                break
        if right == len(A) -1 or left == 0:
            return False
        return A[left] == A[right] and left == right
