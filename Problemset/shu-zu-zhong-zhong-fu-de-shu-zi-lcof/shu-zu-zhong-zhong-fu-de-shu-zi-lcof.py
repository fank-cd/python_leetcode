
# @Title: 数组中重复的数字 (数组中重复的数字 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 11:54:52
# @Runtime: 60 ms
# @Memory: 22.4 MB

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not isinstance(nums,list):
            return False
        for i in range(len(nums)):
            while i !=nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]

�换和是位置和值对应的，这时候出现重复值，可以返回了
                    return nums[i]
                # nums[i],nums[nums[i]] = nums[nums[i]],nums[i]  # 左变右不变，这样是不行的
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
