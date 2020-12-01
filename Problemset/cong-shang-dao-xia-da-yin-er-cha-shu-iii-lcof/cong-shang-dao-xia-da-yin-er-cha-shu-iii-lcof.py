
# @Title: 从上到下打印二叉树 III (从上到下打印二叉树 III LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-28 17:17:15
# @Runtime: 40 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        helper = [root]
        temp = []
        next_level = []
        count = 0

        while helper or next_level:

            if not helper:
                helper = next_level
                next_level = []

            node = helper.pop(0)
            temp.append(node.val)
            if not helper:
                if count % 2 == 0:
                    res.append(temp)
                else:
                    res.append(temp[::-1])
                count +=1
                temp = []
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        return res
