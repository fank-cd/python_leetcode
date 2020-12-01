
# @Title: 三角形的最大周长 (Largest Perimeter Triangle)
# @Author: 2464512446@qq.com
# @Date: 2020-11-29 16:52:14
# @Runtime: 244 ms
# @Memory: 14.7 MB

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0


