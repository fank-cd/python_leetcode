
# @Title: 两数之和 (Two Sum)
# @Author: 2464512446@qq.com
# @Date: 2019-03-01 17:03:28
# @Runtime: 52 ms
# @Memory: 12.1 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        arr = {}
        length = len(nums)
        for i in range(length):
            if (target - nums[i]) in arr:
                return [arr[target - nums[i]], i]
                #print [arr[target-nums[i]],i]
            arr[nums[i]] = i
