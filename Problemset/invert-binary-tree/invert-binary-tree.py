
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-11-05 18:02:53
# @Runtime: 32 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
