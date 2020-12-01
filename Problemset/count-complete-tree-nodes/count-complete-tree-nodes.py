
# @Title: 完全二叉树的节点个数 (Count Complete Tree Nodes)
# @Author: 2464512446@qq.com
# @Date: 2020-11-24 09:56:09
# @Runtime: 92 ms
# @Memory: 20.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if not root:
                return 
            count += 1
            helper(root.left)
            helper(root.right)
        helper(root)
        return count
