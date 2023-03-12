def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    while True:
        s = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '.':
                    s |= {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)}
        if not s:
            break
        answer += len(s)
        for i, j in s:
            board[i][j] = '.'
        for i in range(m-1, 0, -1):
            for j in range(n):
                if board[i][j] == '.':
                    for k in range(i-1, -1, -1):
                        if board[k][j] != '.':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
    return answer
