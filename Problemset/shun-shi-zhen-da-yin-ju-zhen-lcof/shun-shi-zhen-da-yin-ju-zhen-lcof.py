
# @Title: 顺时针打印矩阵 (顺时针打印矩阵  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 16:06:18
# @Runtime: 48 ms
# @Memory: 13.6 MB

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
        
#         def helper(matrix):
#             seen_pos = set()
#             if not matrix:
#                 return 
#             if matrix:
#                 x,y = len(matrix[0]),len(matrix)
#                 p_x,p_y=0,0
            
#                 while p_x < x:
#                     if (p_y,p_x) not in seen_pos:
#                         res.append(matrix[p_y][p_x])
#                         seen_pos.add((p_y,p_x))
#                     p_x += 1
#                 p_x -= 1
#                 while p_y < y:
#                     if (p_y,p_x) not in seen_pos:
#                         res.append(matrix[p_y][p_x])
#                         seen_pos.add((p_y,p_x))
#                     p_y += 1
#                 p_y -= 1
#                 while p_x >= 0:
#                     if (p_y,p_x) not in seen_pos:
#                         res.append(matrix[p_y][p_x])
#                         seen_pos.add((p_y,p_x))
#                     p_x -= 1
#                 p_x +=1
#                 while p_y > 0 :
#                     if (p_y,p_x) not in seen_pos:
#                         res.append(matrix[p_y][p_x])
#                         seen_pos.add((p_y,p_x))
#                     p_y -= 1
            
#             if x > 2 and y >2:
#                 matrix = matrix[1:][:]
#                 matrix = matrix[:-1][:]
#                 temp = []
#                 for i in matrix:
#                     i = i[1:]
#                     i = i[:-1]
#                     temp.append(i)
#                 matrix = temp
#                 helper(matrix)
            
#         helper(matrix)
#         return res

class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        # 更好的解法，而且边界很清晰
        if not matrix: return []

        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): 
                res.append(matrix[t][i]) # left to right
            t += 1
            if t > b:
                 break
            for i in range(t, b + 1): 
                res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1): 
                res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: 
                break
            for i in range(b, t - 1, -1): 
                res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: 
                break
        return res

