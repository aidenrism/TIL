import sys
from pandas import DataFrame as df

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # print(ladder)

    # 도착점 행열 위치 반환하는거 알수있음
    # col, row = 0, 0
    # for c in range(len(ladder)):
    #     for r in range(len(ladder)):
    #         if ladder[c][r] == 2:
    #             col, row = c, r
    # print(col, row)

    d_y = N-1
    d_x = ladder[N-1].index(2)
    move = 0

    # x를 좌우로 움직이는 길 2가지와 두개에 해당 안될때 y축을 상으로 옮기는 방법까지 총 3가지 길
    while d_y >0:
        if (move==0 or move==1) and d_x > 0 and ladder[d_y][d_x-1]:
            d_x -= 1
            move = 1
        elif (move==0 or move==2) and d_x < N-1 and ladder[d_y][d_x+1]:
            d_x += 1
            move = 2
        else:
            d_y -= 1
            move = 0
    print('#{} {}'.format(tc, d_x))

# while True:
#     print(ladder[col][row])
#     if ladder[col-1][row] ==1:
#         col -= 1
#         print(col)
#         continue
#     else:
#         print(col,row)
#         break
    # else:
    #     ladder[col][row-1] == 1:
    #         row -= 1
    #     elif:
    #         ladder[col][row+1] == 1:
    #         row += 1
    # prin(col, row)