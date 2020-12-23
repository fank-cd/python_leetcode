
# @Title: 二叉树的中序遍历 (Binary Tree Inorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-12-01 17:07:27
# @Runtime: 44 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res =[]
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur =  cur.right
        return res
