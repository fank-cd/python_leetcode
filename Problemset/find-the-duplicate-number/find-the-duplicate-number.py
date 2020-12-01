
# @Title: 寻找重复数 (Find the Duplicate Number)
# @Author: 2464512446@qq.com
# @Date: 2019-12-04 18:01:23
# @Runtime: 64 ms
# @Memory: 13.2 MB

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 毫无挑战的排序后查重
        # nums.sort()
        # tmp = None
        # for i in nums:
        #     if i == tmp:
        #         return i
        #     tmp = i

        for i in range(len(nums)):
            while nums[i] != i:  # 下标和值不对应
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # nums[i], nums[nums[i]] = nums[nums[i]],nums[i]
                # 顺序不同会影响结果，需要注意
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return False
