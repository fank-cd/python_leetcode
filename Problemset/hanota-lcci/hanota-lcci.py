
# @Title: 汉诺塔问题 (Hanota LCCI)
# @Author: 2464512446@qq.com
# @Date: 2020-04-01 15:48:59
# @Runtime: 68 ms
# @Memory: 13.8 MB

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)

        def helper(n, A, B, C):
            if n == 1:
                C.append(A.pop())
                return
            else:
                helper(n-1, A, C, B)
                C.append(A.pop())
                helper(n-1, B, A, C)
        helper(n, A, B, C)
