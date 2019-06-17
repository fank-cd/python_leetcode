
# @Title: 第一个错误的版本 (First Bad Version)
# @Author: 2464512446@qq.com
# @Date: 2018-11-30 12:01:21
# @Runtime: 24 ms
# @Memory: N/A

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        best = 0
        
        while low <= high:
            
            guess = (low+high)/2
            mid = guess

            if isBadVersion(guess):
                high = mid -1
                best = guess
            else:
                low = mid + 1
        return best
