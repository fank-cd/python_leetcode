
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



