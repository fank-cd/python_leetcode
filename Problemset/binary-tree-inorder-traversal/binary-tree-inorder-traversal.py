
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
cur.val)
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

