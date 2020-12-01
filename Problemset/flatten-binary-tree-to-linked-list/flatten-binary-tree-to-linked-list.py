
# @Title: 二叉树展开为链表 (Flatten Binary Tree to Linked List)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 11:41:35
# @Runtime: 44 ms
# @Memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        stack = [root]
        pre = None
        while stack:
            cur = stack.pop()
            if pre:
                pre.right = cur
                pre.left = None
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            pre = cur
        return root
