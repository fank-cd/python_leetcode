
# @Title: 最大连续1的个数 (Max Consecutive Ones)
# @Author: 2464512446@qq.com
# @Date: 2019-03-15 09:55:30
# @Runtime: 52 ms
# @Memory: 10.9 MB

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = []
        count = 0
        for i in nums:
            if i == 1:
                count +=1
            else:
                res.append(count)
                count = 0
                
        res.append(count)
        return max(res)
