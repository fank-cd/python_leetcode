
# @Title: x 的平方根 (Sqrt(x))
# @Author: 2464512446@qq.com
# @Date: 2019-11-19 11:35:56
# @Runtime: 48 ms
# @Memory: 13.8 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x // 2

        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left

