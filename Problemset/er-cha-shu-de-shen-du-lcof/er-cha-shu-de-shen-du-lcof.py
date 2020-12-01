
# @Title: 二叉树的深度 (二叉树的深度 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-10-11 16:10:20
# @Runtime: 60 ms
# @Memory: 14.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque()
        res = 0 
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res += 1
        return res
