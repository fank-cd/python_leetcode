
# @Title: 两数之和 (Two Sum)
# @Author: 2464512446@qq.com
# @Date: 2019-07-09 11:30:24
# @Runtime: 60 ms
# @Memory: 14.2 MB

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        用字典来保存列表的值和下标，值为key，下标为value
        遍历一次后去字典中中key，找到则返回下标
        一边遍历一边生成，还可以避免重复的情况
        """
        
        n = len(nums)
        lookup = {}
        for i in range(n):
            tmp = target - nums[i]
            if tmp in lookup:
                return [lookup[tmp], i]
            lookup[nums[i]] = i



