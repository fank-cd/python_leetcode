
# @Title: 两数之和 (Two Sum)
# @Author: 2464512446@qq.com
# @Date: 2019-11-11 15:03:20
# @Runtime: 36 ms
# @Memory: 13.2 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dct = {} # 用字典来存储值和对应的index
        for i, n in enumerate(nums):
            if target - n in dct: # 达成条件
                return [dct[target - n], i]
            dct[n] = i
        
        
        # d = {}
        # for index,i in enumerate(nums):
        #     num = target - i 
        #     if num not in d:
        #         d[i] =index
        #     else:
        #         return [d[num],index]
