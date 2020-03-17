
# @Title: 除自身以外数组的乘积 (Product of Array Except Self)
# @Author: 2464512446@qq.com
# @Date: 2019-12-03 15:04:47
# @Runtime: 120 ms
# @Memory: 18.5 MB

class Solution(object):
    def productExceptSelf(self, nums):

        # 计算左边乘积，再遍历右边时再相乘
        n=len(nums)
        res=[0]*n
        k=1
        for i in range(n):
            res[i]=k
            k=k*nums[i]
        k=1
        # print(res)
        for i in range(n-1,-1,-1):
            res[i]*=k
            k*=nums[i]
        return res

