
# @Title: 三数之和 (3Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:36:38
# @Runtime: 812 ms
# @Memory: 16 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if nums[k] > 0:
                break
            if k >= 1 and nums[k] == nums[k-1]:
                # print(233)
                continue

            i,j = k + 1, len(nums) -1
            while i < j:
                summ = nums[k] + nums[i] + nums[j]
                # print(k,i,j)
                if summ <0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                            i += 1
                elif summ > 0 :
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                            j -= 1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                            i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                            j -= 1
        return res
