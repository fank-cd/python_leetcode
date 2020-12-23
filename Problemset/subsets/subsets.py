
# @Title: 子集 (Subsets)
# @Author: 2464512446@qq.com
# @Date: 2019-11-29 17:53:39
# @Runtime: 24 ms
# @Memory: 11.4 MB

class Solution(object):
    def subsets(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size == 0:
            return []
        res = []
        self.dfs(nums,0,[],res)
        return res

    def dfs(self,nums,start,path,res):
        res.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            self.dfs(nums,i+1,path,res)  # i+1 使得不会复用上一层递归树用过的元素
            path.pop()
