
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 17:09:35
# @Runtime: 20 ms
# @Memory: 11.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not isinstance(root,TreeNode):
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left,root.right = root.right,root.left
        return root
