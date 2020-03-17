
# @Title: 生命游戏 (Game of Life)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 17:29:28
# @Runtime: 16 ms
# @Memory: 11.7 MB

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 蠢蛋写法
        col = len(board)
        row = len(board[0])
        res = []
        boardBackup = copy.deepcopy(board)
        for i in range(col):
            for j in range(row):
                val = board[i][j]
                total = self.pos_vaild(i,j,col,row,boardBackup)
                print(total,i,j)
                if val == 1 and total <2:
                    board[i][j] = 0
                elif val == 1 and total >3:
                    board[i][j] = 0
                elif val == 0 and total == 3:
                    board[i][j] =1


    def pos_vaild(self,i,j,col,row,board):
        total = 0
        if i!=0: # 不在上边界
            total += board[i-1][j]
            # print(1,total)
        if i != col-1: # 不在下边界
            total += board[i+1][j]
            # print(2,total)
        if j !=0 :
            total += board[i][j-1]
            # print(3,total)
        if j != row-1:
            total += board[i][j+1]
            # print(4,total)
        if i != 0 and j != 0:
            total += board[i-1][j-1]
            # print(5,total)
        if i !=0 and j != row-1:
            total += board[i-1][j+1]
            # print(6,total)
        if i != col-1 and j !=0:
            total += board[i+1][j-1]
            # print(7,total)
        if i != col -1 and j != row -1 :
            total += board[i+1][j+1]

            # print(8,total)
        return total



