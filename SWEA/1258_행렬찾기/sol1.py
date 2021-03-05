import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split()))for _ in range(N)]

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
                    temp = c_pot[-1] - c_pot[0] + 1
                    cr_list[c].append(temp)
                    c_pot = []
        # 0 이 아닌 숫자가 있는 인덱스들이 있다면
        if c_pot:
            row = c_pot[-1] - c_pot[0] + 1
            cr_list[c].append(row)

    cnt_list = [[] for _ in range(N)]
    for idx in range(N):
        for jdx in range(len(cr_list[idx])):
            row = cr_list[idx][jdx]
            cnt_list[row].append(row)

    # 작은것부터 행렬 추출
    cnt = 0
    result = [[] for _ in range(N)]
    for i in range(N):
        if cnt_list[i]:
            cnt += 1
            result[i] += [len(cnt_list[i]), i]
    result1 = [[]for _ in range(N)]

    for i in range(N):
        if result[i]:
            area = result[i][0] * result[i][1]
            result1[result[i][0]-1].append(area)
            result1[result[i][0] - 1].append(result[i][0])
            result1[result[i][0] - 1].append(result[i][1])

    result1 = sorted(result1)
    print()
    # print(result1)

    print('#{} {}'.format(tc, cnt), end=' ')
    for i in range(len(result1)):
        if result1[i]:
            print(*result1[i][1:], end=' ')
