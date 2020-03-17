
# @Title: 子集 II (Subsets II)
# @Author: 2464512446@qq.com
# @Date: 2019-11-29 17:54:41
# @Runtime: 20 ms
# @Memory: 11.7 MB

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        nums.sort() # 排序是为了处理剪枝（即重复元素）
        if size == 0:
            return []

        res = []

        self.__dfs(nums,0,[],res)
        # return list(set(res))
        return res

    def __dfs(self,nums,start,path,res):
#        if path not in res:

        res.append(path[:])
        for i in range(start,len(nums)):
            if nums[i] == nums[i-1] and i-1>=start:  # 相比子集I 多了剪枝和排序操作。当然排序也是为了剪枝
                continue
            path.append(nums[i])
            self.__dfs(nums,i+1,path,res) # i+1 使得不会复用上一层递归树用过的元素
            path.pop()
