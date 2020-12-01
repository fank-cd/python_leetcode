
# @Title: 对称二叉树 (Symmetric Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-11-08 12:08:46
# @Runtime: 16 ms
# @Memory: 11.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.core(root,root)
    
    def core(self,node1,node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        
        return self.core(node1.left,node2.right) and self.core(node1.right,node2.left)
