class Solution:
    def dfs(self, r, c, board, visited):
        m, n = len(board), len(board[0])
        if r < 0 or c < 0 or r >= m or c >= n or board[r][c] == 'X' or visited[r][c]:
            return
        
        visited[r][c] = True

        self.dfs(r - 1, c, board, visited)
        self.dfs(r + 1, c, board, visited)
        self.dfs(r, c - 1, board, visited)
        self.dfs(r, c + 1, board, visited)

    def solve(self, board):
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(n):
            if board[0][i] == 'O':
                self.dfs(0, i, board, visited)

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(i, 0, board, visited)

        for i in range(n):
            if board[m - 1][i] == 'O':
                self.dfs(m - 1, i, board, visited)

        for i in range(m):
            if board[i][n - 1] == 'O':
                self.dfs(i, n - 1, board, visited)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'