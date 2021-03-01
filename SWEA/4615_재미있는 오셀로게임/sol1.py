import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    board = [[0] * int(n+2) for _ in range(n+2)]

    cen1, cen2 = int(n/2), int(n/2+1)
    default = [[cen1,cen1,2],[cen2,cen2,2],[cen1,cen2,1],[cen2,cen1,1]]
    # print(default)

    for idx in range(len(default)):
        if default[idx][-1] == 2:
            board[default[idx][0]][default[idx][1]] += 2
        elif default[idx][-1] == 1:
            board[default[idx][0]][default[idx][1]] += 1

    # print(default[0][0])
    # print(board)

    for _ in range(m):
        oslo = list(map(int, input().split()))
        # print(oslo)
        if oslo[-1] == 2:
            board[oslo[0]][oslo[1]] += 2

        else:
            board[oslo[0]][oslo[1]] += 1

            #  # 위 아래
        if oslo[0] == 1 and board[n][oslo[1]] == oslo[-1]:
            inner = []
            for r in range(2, n):
                inner.append(board[r][oslo[1]])
            if oslo[-1] not in inner:

                for i in range(1, 1 + n):
                    board[i][oslo[1]] = oslo[-1]
            elif oslo[0] == n and board[1][oslo[1]] == oslo[-1]:
                for i in range(1, 1 + n):
                    board[i][oslo[1]] = oslo[-1]

            ## 대각선
        if oslo[0:2] == [1, 1] and board[n][n] == oslo[-1]:
            inner = []
            for r in range(2, n):
                inner.append(board[r][r])
            if oslo[-1] not in inner:

                for i in range(1, 1 + n):
                    for j in range(1, 1 + n):
                        if i == j:
                            board[i][j] = oslo[-1]

            elif oslo[0:2] == [n, n] and board[1][1] == oslo[-1]:
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if i == j:
                            board[i][j] = oslo[-1]

            # 역 대각선
        if oslo[0:2] == [1, n] and board[n][1] == oslo[-1]:

            inner = []
            for r in range(2, n):
                for r2 in range(2, n):
                    if r + r2 == n + 1:
                        inner.append(board[r][r2])
                    if oslo[-1] not in inner:

                        for i in range(1, n + 1):
                            for j in range(1, n + 1):
                                if i + j == n + 1:
                                    board[i][j] = oslo[-1]

                    elif oslo[0:2] == [n, n] and board[1][1] == oslo[-1]:
                        for i in range(1, n + 1):
                            for j in range(1, n + 1):
                                if i + j == n + 1:
                                    board[i][j] = oslo[-1]

            # 양 옆
        if oslo[1] == 1 and board[oslo[0]][n] == oslo[-1]:
            inner = []
            for r in range(2, n):
                inner.append(board[oslo[0]][r])
            if oslo[-1] not in inner:

                for i in range(1, 1 + n):
                    board[oslo[0]][i] = oslo[-1]
            elif oslo[1] == n and board[oslo[0]][1] == oslo[-1]:
                for i in range(1, 1 + n):
                    board[oslo[0]][i] = oslo[-1]

        #상하좌우중 두군데이상에서 다른숫자가 있으면 다른숫자로 바뀜
        for k in range(1,len(board)-1):
            for l in range(1,len(board)-1):
                cnt1 = 0
                cnt2 = 0
                if board[k][l] == 0:
                    pass
                else:
                    if board[k-1][l] == 1:
                        cnt1 += 1
                    if board[k+1][l] == 1:
                        cnt1 += 1
                    if board[k][l-1] == 1:
                        cnt1 += 1
                    if board[k][l+1] == 1:
                        cnt1 += 1
                    if cnt1 >= 2:
                        board[k][l] = 1
                    if board[k - 1][l] == 2:
                        cnt2 += 1
                    if board[k + 1][l] == 2:
                        cnt2 += 1
                    if board[k][l - 1] == 2:
                        cnt2 += 1
                    if board[k][l + 1] == 2:
                        cnt2 += 1
                    if cnt2 >= 2:
                        board[k][l] = 2



    count_1 = 0
    count_2 = 0
    for k in range(1,len(board)-1):
        for l in range(1,len(board)-1):

            if board[k][l] == 1:
                count_1 += 1
            elif board[k][l] == 2:
                count_2 += 1
    # result = 0
    # if count_1 > count_2:
    #     result = count_1
    # else:
    #     result = count_2
    print('#{} {} {}'.format(tc, count_1, count_2))
    # print(board)
