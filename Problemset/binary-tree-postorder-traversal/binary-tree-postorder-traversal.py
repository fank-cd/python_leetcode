
# @Title: 二叉树的后序遍历 (Binary Tree Postorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 16:15:11
# @Runtime: 20 ms
# @Memory: 11.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
    #     if not root:
    #         return []
    #     res = []
    #     self.post(root,res)
    #     return res
    # def post(self,root,res):
    #     if not root:
    #         return None
    #     self.post(root.left,res)
    #     self.post(root.right,res)
    #     res.append(root.val)
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
                stack.append((cur,True))
                if cur.right:
                    stack.append((cur.right,False))
                if cur.left:
                    stack.append((cur.left,False))
             
        return res



