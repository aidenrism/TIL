import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # crops = [list(map(int, input().split())) for _ in range(N)]
    crops = [list(map(int, input())) for _ in range(N)]

    # print(crops)
    # print(crops[0][0])

    mid = N // 2
    k = 0
    revenue = []
    # for i in range(N):
    #     for j in range(N):
    #         if i == mid:
    #             revenue.append(crops[i][j])
    #         elif i == 0 or i == N-1:
    #             if j == mid:
    #                 revenue.append(crops[i][mid])
    #         elif i == 1 or i == N-1-1:
    #             if mid-1 <= j <= mid+1:
    #                revenue.append(crops[i][j])
    #     # revenue.append(crops[i][mid])
    # print(revenue)

    while k <= mid:
        for i in range(N):
            for j in range(N):
                if i == k or i == N - 1 - k:
                    if mid - k <= j <= mid + k:
                        revenue.append(crops[i][j])
        k += 1
    print('#{} {}'.format(tc, sum(revenue)))