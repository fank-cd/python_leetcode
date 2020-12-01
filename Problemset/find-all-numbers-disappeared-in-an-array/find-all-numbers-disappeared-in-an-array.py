
# @Title: 找到所有数组中消失的数字 (Find All Numbers Disappeared in an Array)
# @Author: 2464512446@qq.com
# @Date: 2020-03-05 18:32:37
# @Runtime: 660 ms
# @Memory: 20.5 MB

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 自己做的
        # seen = set(nums)
        # nums_all = set([i for i in range(1,len(nums)+1)])
        # res = list(nums_all - seen)
        # return res
        # 不使用额外空间
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        result = []    

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result    

