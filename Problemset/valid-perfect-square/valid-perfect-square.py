
# @Title: 有效的完全平方数 (Valid Perfect Square)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 16:57:47
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not num:
            return False
        left, right = 0, num
        while left <= right:
            mid = left + (right-left) // 2
            sqrt = mid * mid
            if sqrt  == num:
                return True
            elif sqrt < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
