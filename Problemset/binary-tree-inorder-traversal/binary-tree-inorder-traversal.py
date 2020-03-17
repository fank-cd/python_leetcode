
# @Title: 二叉树的中序遍历 (Binary Tree Inorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 16:10:57
# @Runtime: 24 ms
# @Memory: 11.6 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root :
                return []
            stack = [(root,False)]
            res = []
            while stack:
                cur,visited = stack.pop()
                if visited:
                    res.append(cur.val)
                else:
                    if cur.right:
                        stack.append((cur.right,False))
                    stack.append((cur,True))
                    if cur.left:
                        stack.append((cur.left,False))     
            return res
            # 迭代写法
            # res = []
            # stack = []
            # curr = root

            # while(curr!=None or not stack == []):
            #     while (curr != None):
            #         stack.append(curr)
            #         curr = curr.left

            #     curr = stack.pop()
            #     res.append(curr.val)
            #     curr = curr.right

            # return res
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     递归写法
    #     res = []
    #     self.middle(root,res)
    #     return res
    # def middle(self,root,res):
    #     if root is None:
    #         return None
    #     self.middle(root.left,res)
    #     res.append (root.val)
    #     self.middle(root.right,res)

