
# @Title: 在每个树行中找最大值 (Find Largest Value in Each Tree Row)
# @Author: 2464512446@qq.com
# @Date: 2020-11-24 17:23:19
# @Runtime: 64 ms
# @Memory: 15.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack  = [root]
        while stack:
            math_max = -math.inf
            for i in range(len(stack)):
                root = stack.pop(0)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                math_max = max(math_max,root.val)
            res.append(math_max)
        return res
