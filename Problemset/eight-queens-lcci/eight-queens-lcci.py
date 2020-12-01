
# @Title: 八皇后 (Eight Queens LCCI)
# @Author: 2464512446@qq.com
# @Date: 2020-04-02 10:54:08
# @Runtime: 248 ms
# @Memory: 13.6 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for i in range(n)]
        # print(board)
        # for i in range(n):
        #     res = ""
        #     for j in range(n):
        #         res += "."
        #     board.append(res)
        # print(board)

        def judge(x,y):
            for i in range(n):
                if board[x][i] == "Q":
                    return False
                if board[i][y] == "Q":
                    return False
                if x+y -i <=n-1:
                    if board[i][x+y-i] == "Q":
                        return False
            for index, i in enumerate(range(x-1,-1,-1),start=1):
                s_y = y - index
                if s_y >= 0:
                    if board[i][s_y] == "Q":
                        return False
            return True

        def helper(step):
            if step == n:
                # import copy
                temp = []
                for i in board:
                    temp.append("".join(i))
                # print(1111)
                res.append(temp)
                return 
            for i in range(n):
                if judge(step,i):
                    # print(step,board)
                    # print(board[step])
                    board[step][i] = "Q"
                    helper(step+1)
                    board[step][i] = "."
                    # print(res)
                    # return board
        res = []
        helper(0)
        return res
