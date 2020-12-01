
# @Title: 合并二叉树 (Merge Two Binary Trees)
# @Author: 2464512446@qq.com
# @Date: 2020-09-23 11:09:31
# @Runtime: 104 ms
# @Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        mergeroot = TreeNode(t1.val + t2.val)
        mergeroot.left = self.mergeTrees(t1.left,t2.left)
        mergeroot.right = self.mergeTrees(t1.right,t2.right)
        return mergeroot
