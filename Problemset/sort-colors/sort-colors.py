
# @Title: 颜色分类 (Sort Colors)
# @Author: 2464512446@qq.com
# @Date: 2019-12-16 12:28:57
# @Runtime: 20 ms
# @Memory: 11.8 MB

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 自己的办法
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] not in d:
        #         d[nums[i]] = []
        #     d[nums[i]].append(i)

        # p = 0
        # for k,v in d.items():
        #     for i in v:
        #         nums[p] = k
        #         p +=1

        p0,curr = 0,0
        p1= len(nums) -1

        while curr <= p1:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                p1 -= 1
            else:
                curr += 1

