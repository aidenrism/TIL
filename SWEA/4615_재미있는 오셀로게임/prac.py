#  # 위 아래
    if othello[0] == 1 and board[n][othello[1]] == othello[-1]:
        inner = []
        for r in range(2, n):
            inner.append(board[r][othello[1]])
        if othello[-1] not in inner:

            for i in range(1, 1 + n):
                board[i][othello[1]] = othello[-1]
        elif othello[0] == n and board[1][othello[1]] == othello[-1]:
            for i in range(1, 1 + n):
                board[i][oslo[1]] = othello[-1]

    ## 대각선
    if othello[0:2] == [1, 1] and board[n][n] == othello[-1]:
        inner = []
        for r in range(2, n):
            inner.append( board[r][r])
        if othello[-1] not in inner:

            for i in range(1, 1 + n):
                for j in range(1, 1 + n):
                    if i == j:
                        board[i][j] = othello[-1]

        elif othello[0:2] == [n, n] and board[1][1] == othello[-1]:
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i == j:
                        board[i][j] = othello[-1]

    # 역 대각선
    if othello[0:2] == [1, n] and board[n][1] == othello[-1]:

        inner = []
        for r in range(2, n):
            for r2 in range(2, n):
                if r + r2 == n + 1
                    inner.append(board[r][r2])
                if othello[-1] not in inner:

                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if i + j == n + 1:
                                board[i][j] = othello[-1]

                elif othello[0:2] == [n, n] and board[1][1] == othello[-1]:
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if i + j == n + 1:
                                board[i][j] = othello[-1]

    # 양 옆
    if othello[1] == 1 and board[othello[0]][n] == othello[-1]:
        inner = []
        for r in range(2, n):
            inner.append(board[othello[0]][r])
        if othello[-1] not in inner:

            for i in range(1, 1 + n):
                board[othello[0]][i] = othello[-1]
        elif othello[1] == n and board[othello[0]][1] == othello[-1]:
            for i in range(1, 1 + n):
                board[othello[0]][i] = othello[-1]

