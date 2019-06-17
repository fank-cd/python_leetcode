
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-03-12 11:28:13
# @Runtime: 44 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        lep = self.maxDepth(root.left)
        rep = self.maxDepth(root.right)
        
        return max(lep,rep)+1
