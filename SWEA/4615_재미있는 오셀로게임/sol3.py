import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        r, c, g = map(int, input().split())
        r, c = r - 1, c - 1
        board[c][r] = g
        g2 = 2 if g - 2 else 1

        # 상 하
        m = 1
        change = False
        while c - m > 0 and board[c - m][r] == g2:
            m += 1
            if board[c - m][r] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c - i][r] = g

        m = 1
        change = False
        while c + m < N - 1 and board[c + m][r] == g2:
            m += 1
            if board[c + m][r] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c + i][r] = g

        # 좌 우
        m = 1
        change = False
        while r - m > 0 and board[c][r - m] == g2:
            m += 1
            if board[c][r - m] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c][r - i] = g

        m = 1
        change = False
        while r + m < N - 1 and board[c][r + m] == g2:
            m += 1
            if board[c][r + m] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c][r + i] = g

        # 좌상 우하
        m = 1
        change = False
        while c - m > 0 and r - m > 0 and board[c - m][r - m] == g2:
            m += 1
            if board[c - m][r - m] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c - i][r - i] = g

        m = 1
        change = False
        while c + m < N - 1 and r + m < N - 1 and board[c + m][r + m] == g2:
            m += 1
            if board[c + m][r + m] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c + i][r + i] = g

        # 우상 좌하
        m = 1
        change = False
        while c - m > 0 and r + m < N - 1 and board[c - m][r + m] == g2:
            m += 1
            if board[c - m][r + m] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c - i][r + i] = g

        m = 1
        change = False
        while c + m < N - 1 and r - m > 0 and board[c + m][r - m] == g2:
            m += 1
            if board[c + m][r - m] == g:
                change = True
                break
        if change:
            for i in range(1, m):
                board[c + i][r - i] = g

    cnt = [0] * 3

    for i in range(N):
        for j in range(len(board[i])):
            cnt[board[i][j]] += 1

    print('#{} {} {}'.format(tc, cnt[1], cnt[2]))

