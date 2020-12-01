
# @Title: 二叉搜索树与双向链表 (二叉搜索树与双向链表  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-07-02 10:47:00
# @Runtime: 52 ms
# @Memory: 14.4 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# class Solution:
#     def treeToDoublyList(self, root: 'Node') -> 'Node':
#         if not root:
#             return None
#         res = []
#         def dfs(root):
#             if not root:
#                 return 
#             dfs(root.left)
#             res.append(root)
#             dfs(root.right)

#         dfs(root)
    
#         if len(res) < 2:
#             res[0].left = res[0]
#             res[0].right = res[0]
#             return res[0]
#         # print(res)
#         p1,p2 = 0,1
#         last = len(res)-1
#         res[last].right = res[p1]
#         res[p1].left = res[last]
#         while p2 < len(res):
#             res[p2].left = res[p1]
#             res[p1].right = res[p2]
#             p1 += 1
#             p2 += 1
#         return res[0]
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head



