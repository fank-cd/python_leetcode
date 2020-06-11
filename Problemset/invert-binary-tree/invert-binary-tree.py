
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-06-11 18:01:23
# @Runtime: 44 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        root.left,root.right=root.right,root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
