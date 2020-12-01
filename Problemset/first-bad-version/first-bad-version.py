
# @Title: 第一个错误的版本 (First Bad Version)
# @Author: 2464512446@qq.com
# @Date: 2020-09-07 15:50:06
# @Runtime: 36 ms
# @Memory: 13.4 MB

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n
        while left <= right:
            mid = left  +(right -left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left
