
# @Title: 路径总和 (Path Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-11-29 16:28:24
# @Runtime: 56 ms
# @Memory: 15.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def helper(root, path):
            if not root:
                return False
            path += root.val
            if not root.left and not root.right:
                if path == sum:
                    return True
            return helper(root.left,path) or helper(root.right,path)
        return helper(root, 0)
        

