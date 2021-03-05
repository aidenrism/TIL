import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().split()))for _ in range(N)]
    print(matrix)

    # 각 행의 창고 행 길이를 저장
    cr_list = [[] for _ in range(N)]

    for c in range(N):
        # 각 행의 0이 아닌 숫자의 인덱스를 저장
        c_pot = []
        for r in range(N):
            if matrix[c][r] != 0:
                # 창고에 인덱스들을 저장
                c_pot.append(r)
            # 저장하다가 0이 나오면 마지막 인덱스 값+1 저장 (창고의 행길이)
            elif matrix[c][r] == 0:
                while c_pot:
                    # print(c_pot)
                    cr_list[c].append((c_pot.pop())+1)
                    c_pot = []
        # 0 이 아닌 숫자가 있는 인덱스들이 있다면
        if c_pot:
            row = c_pot[-1] - c_pot[0] + 1
            cr_list[c].append(row)
    # print(cr_list)

    cnt_list = [[] for _ in range(N)]
    for idx in range(N):
        for jdx in range(len(cr_list[idx])):
            row = cr_list[idx][jdx]
            cnt_list[row].append(row)
            # cnt1 += 1

    # print(cnt_list)

    # print('#{}'.format(tc), end=' ')
    # 작은것부터 행렬 추출
    cnt = 0
    result = [[] for _ in range(N)]
    for i in range(N):
        if cnt_list[i]:
            cnt += 1
            result[i] += [len(cnt_list[i]), i]

    # print()
    # print(result)
    # print(cnt, *result)

    # for i in range(N):
    #     for j in range(len(result[i])):
    #         if result[i]:
    #             print(result[i][j])

    result1 = [[]for _ in range(cnt)]
    # print(result1)
    for i in range(N):
        if result[i]:
            area = result[i][0] * result[i][1]
            # print(area,result[i][0])
            # result1[result[i][0]-1].append(area)
            # result1[result[i][0] - 1].append(result[i][0])
            # result1[result[i][0] - 1].append(result[i][1])

    # print(result1)
    # print(len(result1))
    result1 = sorted(result1)
    # print(result1)
    # print(len(result1))
    # for i in range(len(result1)):
    #     print(*result1[i][1:], end=' ')





















#
# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     matrix = [list(map(int, input().split()))for _ in range(N)]
#     # print(matrix)
#
#     # 각 행의 창고 행 길이를 저장
#     cr_list = [[] for _ in range(N)]
#
#     for c in range(N):
#         # 각 행의 0이 아닌 숫자의 인덱스를 저장
#         c_pot = []
#         for r in range(N):
#             if matrix[c][r] != 0:
#                 # 창고에 인덱스들을 저장
#                 c_pot.append(r)
#             # 저장하다가 0이 나오면 마지막 인덱스 값+1 저장 (창고의 행길이)
#             elif matrix[c][r] == 0:
#                 while c_pot:
#                     # print(c_pot)
#                     cr_list[c].append((c_pot.pop())+1)
#                     c_pot = []
#         # 0 이 아닌 숫자가 있는 인덱스들이 있다면
#         if c_pot:
#             row = c_pot[-1] - c_pot[0] + 1
#             cr_list[c].append(row)
#     # print(cr_list)
#
#     cnt_list = [[] for _ in range(N)]
#     for idx in range(N):
#         for jdx in range(len(cr_list[idx])):
#             row = cr_list[idx][jdx]
#             cnt_list[row].append(row)
#
#     # print(cnt_list)
#     print('#{}'.format(tc), end=' ')
#     # 작은것부터 행렬 추출
#     for i in range(N):
#         if cnt_list[i]:
#
#             print(i,len(cnt_list[i]), end=' ')
#     print()
#
#
#     #     for j in range(len(cnt_list[i])):
#     #         if cnt_list[i]:
#     #             print(len(cnt_list[i]),i)