
# @Title: 数组中重复的数字 (数组中重复的数字 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-04-20 11:38:03
# @Runtime: 28 ms
# @Memory: 19.9 MB

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not isinstance(nums,list):
            return 
        for i in range(len(nums)):
            while i  != nums[i]:  # 位置和值不对应
                if nums[i] == nums[nums[i]]:  # nums[i]交换和是位置和值对应的，这时候出现重复值，可以返回了
                    return nums[i]
                # nums[i],nums[nums[i]] = nums[nums[i]],nums[i]  # 左变右不变，这样是不行的
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
