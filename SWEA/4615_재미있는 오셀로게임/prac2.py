# oslo = [[1,1],2]
#
# print(oslo[0:2])
#
# if oslo[0:2] == [1,1]:
#     print('ok')
# print(oslo[0][1])
#
# n = 4
# ooss = [1, 1, 2]
#
#
# for i in range(n-2):
#     test_c_i = 1 + 1
#     print(test_c_i)
# imm = []
# for i in range(2):
#     imm.append(oslo[0][i])
# print(imm)
#
# cu = 1
# if cu not in ooss:
#     print('noooo')
# else:
#     print('gogo')


# c = 2
# c1 = 1
#
# x = 'yes' if c- 2 else 'no'
# print(x)
import  sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        x, y, c = map(int, input().split())
        x, y = x - 1, y - 1
        board[y][x] = c
        c2 = 2 if c - 2 else 1

        # 위
        m = 1
        change = False
        while y - m > 0 and board[y - m][x] == c2:
            m += 1
            if board[y - m][x] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y - i][x] = c

        # 아래
        m = 1
        change = False
        while y + m < N - 1 and board[y + m][x] == c2:
            m += 1
            if board[y + m][x] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y + i][x] = c

        # 왼쪽
        m = 1
        change = False
        while x - m > 0 and board[y][x - m] == c2:
            m += 1
            if board[y][x - m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y][x - i] = c

        # 오른쪽
        m = 1
        change = False
        while x + m < N - 1 and board[y][x + m] == c2:
            m += 1
            if board[y][x + m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y][x + i] = c

        # 왼위
        m = 1
        change = False
        while x - m > 0 and y - m > 0 and board[y - m][x - m] == c2:
            m += 1
            if board[y - m][x - m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y - i][x - i] = c

        # 오위
        m = 1
        change = False
        while x + m < N - 1 and y - m > 0 and board[y - m][x + m] == c2:
            m += 1
            if board[y - m][x + m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y - i][x + i] = c

        # 왼아래
        m = 1
        change = False
        while x - m > 0 and y + m < N - 1 and board[y + m][x - m] == c2:
            m += 1
            if board[y + m][x - m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y + i][x - i] = c

        # 오아래
        m = 1
        change = False
        while x + m < N - 1 and y + m < N - 1 and board[y + m][x + m] == c2:
            m += 1
            if board[y + m][x + m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y + i][x + i] = c

    count = [0] * 3
    for i in range(N):
        for n in board[i]:
            count[n] += 1
    print('#{} {} {}'.format(test_case, count[1], count[2]))