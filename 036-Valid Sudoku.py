# coding:utf-8

# 有效的数独

# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
#     数字 1-9 在每一行只能出现一次。
#     数字 1-9 在每一列只能出现一次。
#     数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
# 上图是一个部分填充的有效的数独。
#
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
# 示例 1:
#
# 输入:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
#
# 示例 2:
#
# 输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
#      但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
#
# 说明:
#
#     一个有效的数独（部分已被填充）不一定是可解的。
#     只需要根据以上规则，验证已经填入的数字是否有效即可。
#     给定数独序列只包含数字 1-9 和字符 '.' 。
#     给定数独永远是 9x9 形式的。


# 思路是用一个字典来保存数字是否被占用，为“.”则不考虑。
# 依次遍历横排、竖排、以及九宫格

# 笨蛋解法

# def isValidSudoku(self, board):
#     """
#     :type board: List[List[str]]
#     :rtype: bool
#     """
#
#     is_ok = True
#     for i in range(9):
#         number_state1 = {"1": True, "2": True, "3": True, "4": True, "5": True, "6": True, "7": True, "8": True,
#                          "9": True, ".": True}
#
#         for k in range(9):
#             if board[i][k] != ".":
#                 if number_state1[board[i][k]] == True:
#                     number_state1[board[i][k]] = False
#                 else:
#                     is_ok = False
#
#     for i in range(9):
#         number_state2 = {"1": True, "2": True, "3": True, "4": True, "5": True, "6": True, "7": True, "8": True,
#                          "9": True
#             , ".": True}
#         for k in range(9):
#
#             if board[k][i] != ".":
#                 if number_state2[board[k][i]] == True:
#                     number_state2[board[k][i]] = False
#                 else:
#                     is_ok = False
#     for i in range(9):
#
#         number_state3 = {"1": True, "2": True, "3": True, "4": True, "5": True, "6": True, "7": True, "8": True,
#                          "9": True, ".": True}
#         for k in range(9):
#
#             x = 3 * (i / 3) + k / 3
#             y = 3 * (i % 3) + k % 3
#             if board[x][y] != ".":
#                 if number_state3[board[x][y]] == True:
#                     number_state3[board[x][y]] = False
#                 else:
#                     is_ok = False
#
#     return is_ok

# 优雅解法
# 遍历一遍即可，存储每一行，每一列，每一小格子的数字出现的次数
# 大于2则False
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    row = [{} for i in range(9)]
    column = [{} for i in range(9)]
    box = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != ".":
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                row[i][num] = row[i].get(num, 0) + 1

                column[j][num] = column[j].get(num, 0) + 1

                box[box_index][num] = box[box_index].get(num, 0) + 1

                if row[i][num] > 1 or column[j][num] > 1 or box[box_index][num] > 1:
                    return False

    return True
