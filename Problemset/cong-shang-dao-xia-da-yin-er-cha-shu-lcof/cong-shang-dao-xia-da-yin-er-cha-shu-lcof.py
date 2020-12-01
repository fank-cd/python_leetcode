
# @Title: 从上到下打印二叉树 (从上到下打印二叉树 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 17:59:35
# @Runtime: 48 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         res = [root]
#         out = [root.val]
#         while res:
#             node = res.pop(0)
#             # print(out)
#             if not node:
#                 continue
#             if node.left:
#                 res.append(node.left)

#                 out.append(node.left.val)
#             if node.right:
#                 res.append(node.right)
#                 out.append(node.right.val)

#         return out

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        return res

