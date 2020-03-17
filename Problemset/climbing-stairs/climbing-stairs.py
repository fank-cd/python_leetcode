
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: 2464512446@qq.com
# @Date: 2019-11-08 16:56:53
# @Runtime: 24 ms
# @Memory: 11.8 MB

class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n ==1:
#             return 1
#         if n == 2:
#             return 2
        
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)
        def climbStairs(self, n):
            i,j = 1,2
            
            for _ in range(3,n):
                i,j = j , i+j
                
            if n > 2:
                return i +j
            else:
                return n 
