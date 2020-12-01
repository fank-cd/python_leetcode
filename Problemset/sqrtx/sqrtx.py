
# @Title: x 的平方根 (Sqrt(x))
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 17:00:58
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x 
        res = 0
        while left <= right:
            mid =  left + (right-left)//2
            sqrt = mid * mid
            if sqrt <= x:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res
