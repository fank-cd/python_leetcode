
# @Title: 对称二叉树 (Symmetric Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-03-11 15:07:00
# @Runtime: 32 ms
# @Memory: 11 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        # :type root: TreeNode
        # :rtype: bool
        return self.isMirror(root,root)
    def isMirror(self,t1,t2):
        if not t1 and not t2: return True
        elif not t1 or not t2: return False
        return t1.val==t2.val and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)
