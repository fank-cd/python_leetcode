
# @Title: 全排列 (Permutations)
# @Author: 2464512446@qq.com
# @Date: 2019-11-29 17:55:36
# @Runtime: 28 ms
# @Memory: 11.6 MB

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        size = len(nums)
        if size == 0:
            return []
        res = []
        used = [False] * len(nums) # 这个used是为了处理不复用本层元素
        self.__dfs(nums,[],used,res)
        return res


    def __dfs(self,nums,path,used,res):
        if len(path) == len(nums):
            res.append(path[:])
            return 
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.__dfs(nums,path,used,res)
                path.pop()
                used[i] = False  # 回溯后其实就可以复用上层元素了
