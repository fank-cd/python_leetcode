
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:49:49
# @Runtime: 56 ms
# @Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
