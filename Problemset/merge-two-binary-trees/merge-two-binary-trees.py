
# @Title: 合并二叉树 (Merge Two Binary Trees)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 15:45:31
# @Runtime: 68 ms
# @Memory: 12.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2 :
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        return t1 or t2