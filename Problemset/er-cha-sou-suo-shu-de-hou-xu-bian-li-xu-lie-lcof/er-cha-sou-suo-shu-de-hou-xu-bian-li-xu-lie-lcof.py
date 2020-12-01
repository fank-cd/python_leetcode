
# @Title: 二叉搜索树的后序遍历序列 (二叉搜索树的后序遍历序列 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-28 18:25:48
# @Runtime: 44 ms
# @Memory: 13.5 MB

# class Solution:
#     def verifyPostorder(self, postorder: List[int]) -> bool:
#         if not postorder:
#             return True

#         root = postorder[-1]
#         leng = len(postorder) -1
#         left = []
#         right = []
#         index = 0
#         for index,i in enumerate(postorder[:-1]):
#             if i < root:
#                 left.append(i)
#             else:
#                 # index = index
#                 break
        
#         for i in range(index,leng):
#             if postorder[i] < root:
#                 return False
#             right.append(postorder[i])

#         return self.verifyPostorder(left) and self.verifyPostorder(right)


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


