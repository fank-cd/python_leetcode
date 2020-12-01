
# @Title: 单词搜索 (Word Search)
# @Author: 2464512446@qq.com
# @Date: 2020-04-28 17:18:25
# @Runtime: 144 ms
# @Memory: 14.9 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        cols = len(board[0])
        rows = len(board)

        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i - 1 >= 0 and visited[i - 1][j] == False and board[i - 1][j] == word[index]: #上
                index += 1
                visited[i - 1][j] = True
                if dfs(i - 1, j, index):
                    return True
                index -= 1
                visited[i - 1][j] = False

            if j + 1 < cols and visited[i][j + 1] == False and board[i][j + 1] == word[index]: #右
                index += 1
                visited[i][j + 1] = True
                if dfs(i, j + 1, index):
                    return True
                index -= 1
                visited[i][j + 1] = False

            if i + 1 < rows and visited[i + 1][j] == False and board[i + 1][j] == word[index]: #下
                index += 1
                visited[i + 1][j] = True
                if dfs(i + 1, j, index):
                    return True
                visited[i + 1][j] = False
                index -= 1

            if j - 1 >= 0 and visited[i][j - 1] == False and board[i][j - 1] == word[index]: #左

                index += 1
                visited[i][j - 1] = True
                if dfs(i, j - 1, index):
                    return True
                index -= 1
                visited[i][j - 1] = False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    visited[i][j] = False
        return False
