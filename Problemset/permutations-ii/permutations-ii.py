
# @Title: 全排列 II (Permutations II)
# @Author: 2464512446@qq.com
# @Date: 2019-11-29 17:57:08
# @Runtime: 44 ms
# @Memory: 11.5 MB

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        used = [False] * len(nums)
        res = []
        # 修改 1：首先排序，之后才有可能发现重复分支，升序、倒序均可
        nums.sort()
        self.__dfs(nums,0,[],used,res)
        return res


    def __dfs(self, nums, index, pre,used,res):
        if index == len(nums):
            res.append(pre[:])
            return

        for i in range(len(nums)):
                # 修改 2：因为排序以后重复的数一定不会出现在开始，故 i > 0
                # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
                # 这种情况跳过即可
                # 剪枝

                
                # 同层相邻相等，且相邻元素已经使用，则可剪枝
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
            if not used[i]:
                used[i] = True
                pre.append(nums[i])
                self.__dfs(nums,index+1, pre, used, res)
                used[i] = False
                pre.pop()
