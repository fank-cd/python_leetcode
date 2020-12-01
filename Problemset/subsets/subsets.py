
# @Title: 子集 (Subsets)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:39:39
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)

        def helper(index,path):
            res.append(path[:])
            for i in range(index,size):
                path.append(nums[i])
                helper(i+1,path)
                path.pop()
        helper(0,[])
        return res
