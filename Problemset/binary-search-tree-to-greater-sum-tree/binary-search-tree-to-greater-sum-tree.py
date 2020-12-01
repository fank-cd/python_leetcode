
# @Title: 把二叉搜索树转换为累加树 (Binary Search Tree to Greater Sum Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-09-21 15:31:07
# @Runtime: 44 ms
# @Memory: 13.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        total = 0
        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)
        
        dfs(root)
        return root
