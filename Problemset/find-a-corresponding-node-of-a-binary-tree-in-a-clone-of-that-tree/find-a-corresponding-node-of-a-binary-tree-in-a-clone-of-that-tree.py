
# @Title: 找出克隆二叉树中的相同节点 (Find a Corresponding Node of a Binary Tree in a Clone of That Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-10-28 15:27:31
# @Runtime: 604 ms
# @Memory: 23.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if target is original:
            return cloned
        return self.getTargetCopy(original.left,cloned.left,target) or self.getTargetCopy(original.right,cloned.right,target)
