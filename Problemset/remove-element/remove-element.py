
# @Title: 移除元素 (Remove Element)
# @Author: 2464512446@qq.com
# @Date: 2019-03-06 10:44:18
# @Runtime: 40 ms
# @Memory: 10.7 MB

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n  -= 1
                
            else:
                i += 1
                
                
        return n
                
