
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 17:47:19
# @Runtime: 36 ms
# @Memory: 14.6 MB

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
        if not isinstance(root,TreeNode):
            return 0
        depth = 1
        depth += max(self.maxDepth(root.left),self.maxDepth(root.right))
        return depth
    

