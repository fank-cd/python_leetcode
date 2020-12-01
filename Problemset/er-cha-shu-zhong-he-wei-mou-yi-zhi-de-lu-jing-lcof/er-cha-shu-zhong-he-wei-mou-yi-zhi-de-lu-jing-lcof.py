
# @Title: 二叉树中和为某一值的路径 (二叉树中和为某一值的路径 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-30 15:43:23
# @Runtime: 60 ms
# @Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []

        def helper(root,target):
            if not root:
                return 
            
            target -= root.val
            path.append(root.val)

            if target == 0 and not root.left and not root.right:
                res.append(path[:])

            helper(root.left,target)
            helper(root.right,target)
            path.pop()

        helper(root,sum)
        return res
