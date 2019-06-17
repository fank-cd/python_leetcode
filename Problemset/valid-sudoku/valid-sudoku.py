
# @Title: 有效的数独 (Valid Sudoku)
# @Author: 2464512446@qq.com
# @Date: 2019-03-07 11:19:25
# @Runtime: 84 ms
# @Memory: 10.7 MB

class Solution(object):
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
                    box_index = (i//3)*3 + j//3
                    
                    
                    row[i][num] = row[i].get(num,0) +1

                    column[j][num] = column[j].get(num,0) +1

                    box[box_index][num] = box[box_index].get(num,0) +1


                    if row[i][num] > 1 or column[j][num] >1 or box[box_index][num] >1:
                        return False
                    
                    
        return True
