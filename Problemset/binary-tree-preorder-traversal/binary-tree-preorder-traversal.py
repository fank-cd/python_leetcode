
# @Title: 二叉树的前序遍历 (Binary Tree Preorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 16:12:28
# @Runtime: 16 ms
# @Memory: 11.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 遍历写法
        if not root:
            return []
        res = []
        stack = [(root,False)]
        while stack:
            cur,visted = stack.pop()
            if visted:
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
