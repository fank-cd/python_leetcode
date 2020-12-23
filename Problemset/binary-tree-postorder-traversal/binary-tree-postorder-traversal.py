
# @Title: 二叉树的后序遍历 (Binary Tree Postorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-11-17 11:47:25
# @Runtime: 36 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]
