
# @Title: 二叉搜索树中的搜索 (Search in a Binary Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-09-29 11:29:33
# @Runtime: 72 ms
# @Memory: 15.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not isinstance(root,TreeNode):
            return None
        if root.val < val:
            return self.searchBST(root.right,val)
        if root.val > val:
            return self.searchBST(root.left,val)
        
        return root

