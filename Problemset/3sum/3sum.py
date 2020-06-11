
# @Title: 三数之和 (3Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-06-06 23:32:26
# @Runtime: 1036 ms
# @Memory: 16.3 MB

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, k = [], 0
        
        for k in range(len(nums) - 2):
            if nums[k] > 0: 
                break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: 
                continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: # 去重
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:  # 去重
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: # 去重
                        i += 1
                    while i < j and nums[j] == nums[j + 1]: # 去重
                        j -= 1
        return res

