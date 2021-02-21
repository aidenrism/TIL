import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    # print(flies)

    col, row = 0, 0


    def my_max(x):
        big = x[0]
        for idx in range(len(x)):
            if x[idx] > big:
                big = x[idx]
        return  big

    catch_list = []

    for _ in range(N-M+1):
        row = 0
        for _ in range(N-M+1):
            total = 0
            for m1 in range(M):
                for m2 in range(M):
                    total += flies[col+m1][row+m2]
            catch_list.append(total)
            row += 1
        col += 1

    print('#{} {}'.format(tc, my_max(catch_list)))