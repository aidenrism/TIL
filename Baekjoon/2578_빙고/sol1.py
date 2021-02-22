import sys
sys.stdin = open('input.txt')


bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]
# 2차원 리스트
print(bingo)
print(check)

check_lst = []
for i in range(len(check)):
    for j in range(len(check[0])):check_lst.append(check[i][j])
# print(check_lst)

cnt = 0
result = []
line_cnt4 = 0
for idx in check_lst:
    cnt += 1
    # 가로로 빙고 세기
    line_cnt3 = 0

    for i in range(len(bingo)):
        line_cnt1 = 0
        line_cnt2 = 0
        for j in range(len(bingo[0])):
            if bingo[i][j] == idx:
                bingo[i][j] = 1
            line_cnt1 += bingo[i][j]
            line_cnt2 += bingo[j][i]
            if line_cnt1 == 5:
                result.append(1)
            if line_cnt2 == 5:
                result.append(1)
            if i == j:
                line_cnt3 += bingo[i][j]
                if line_cnt3 == 5:
                    result.append(1)
    for ldx in range(len(bingo)):
        for jdx in range(len(bingo)-1,-1,-1):
            if ldx == 0 and jdx == 4:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 1 and jdx ==3:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 2 and jdx == 2:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 3 and jdx == 1:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 4 and jdx == 1:
                line_cnt4 += bingo[ldx][jdx]
                break
    if line_cnt4 == 5:
        result.append(1)
    # 세로로 빙고 세기
    # for i in range(len(bingo)):
    #     line_cnt = 0
    #     for j in range(len(bingo[0])):
    #         if bingo[j][i] == idx:
    #             bingo[i][j] = 1
    #         line_cnt += bingo[i][j]
    #         if line_cnt == 5:
    #             result.append(1)
    # 정방향 대각선 빙고 세기
    # 역방향 대각선 빙고 세기
    # for i in range(len(bingo)):
    #     for j in range(len(bingo[0])):
    #         if bingo[i][j] == idx:
    #             bingo[i][j] = 1
    #             cnt += 1
    #             break
    #     if bingo[i][j] == 1:
    #         break
    # if total == 3:
    #     print(cnt)
    # print(result)
    if len(result) == 3:
        print(cnt+3)
        break

