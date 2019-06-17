
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2019-03-06 10:19:43
# @Runtime: 56 ms
# @Memory: 12.4 MB

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0: return 0
        i = 0
        for j in xrange(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
                
        return i +1
