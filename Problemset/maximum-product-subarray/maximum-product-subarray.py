
# @Title: 乘积最大子数组 (Maximum Product Subarray)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:52:01
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        imin = imax = 1
        for i in nums:
            if i < 0:
                imin,imax = imax,imin
            imax = max(i,imax*i)
            imin = min(i,imin*i)
            res = max(res,imax)
        return res
