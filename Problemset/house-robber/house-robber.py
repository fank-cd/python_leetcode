
# @Title: 打家劫舍 (House Robber)
# @Author: 2464512446@qq.com
# @Date: 2018-12-26 15:19:27
# @Runtime: 24 ms
# @Memory: 7 MB

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        res = [0 for x in range(leng)]
        
        if leng >2:
            res[0] = nums[0]
            res[1] = max(nums[0],nums[1])
            
            for i in range(2,leng):
                res[i] = max(res[i-2]+nums[i],res[i-1])
            return res[leng-1]
        else:
            if leng == 2:
                return max(nums[0],nums[1])
            elif leng ==1:
                return nums[0]
            else:
                return 0
        
