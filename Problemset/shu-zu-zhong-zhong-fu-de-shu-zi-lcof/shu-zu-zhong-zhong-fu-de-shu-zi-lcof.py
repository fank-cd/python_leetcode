
# @Title: 数组中重复的数字 (数组中重复的数字 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 11:54:52
# @Runtime: 60 ms
# @Memory: 23 MB

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not isinstance(nums,list):
            return False
        for i in range(len(nums)):
            while i !=nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]

