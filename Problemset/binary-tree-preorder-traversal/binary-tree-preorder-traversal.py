
# @Title: 二叉树的前序遍历 (Binary Tree Preorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-11-17 11:46:20
# @Runtime: 44 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        cur = root
        stack = []
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res
res.append(cur.val)
            else:
                if cur.right:
                    stack.append((cur.right,False))
                if cur.left:
                    stack.append((cur.left,False))
                stack.append((cur,True))

        return res




    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     递归写法
    #     res = []
    #     self.pre(root,res)
    #     return res
    # def pre(self,root,res):
    #     if root is None:
    #         return None
    #     res.append(root.val)
    #     self.pre(root.left,res)
    #     self.pre(root.right,res)
