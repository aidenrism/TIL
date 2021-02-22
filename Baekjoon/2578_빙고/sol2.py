import sys
sys.stdin = open('input.txt')


def finder(ptable):
    bingoCount = 0
    for Py in range(5):
        if (ptable[Py][0] == ptable[Py][1] == ptable[Py][2] == ptable[Py][3] == ptable[Py][4] == 1):
            bingoCount += 1

    for Px in range(5):
        if (ptable[0][Px] == ptable[1][Px] == ptable[2][Px] == ptable[3][Px] == ptable[4][Px] == 1):
            bingoCount += 1

    if (ptable[0][0] == ptable[1][1] == ptable[2][2] == ptable[3][3] == ptable[4][4] == 1):
        bingoCount += 1

    if (ptable[0][4] == ptable[1][3] == ptable[2][2] == ptable[3][1] == ptable[4][0] == 1):
        bingoCount += 1

    return bingoCount


bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]
# 2차원 리스트
# print(bingo)
# print(check)

# 체크 리스트에 값들을 인덱스 순서대로 더해줌. 나중에  for문을 쉽게 돌리려고
check_lst = []
for i in range(len(check)):
    for j in range(len(check[0])):check_lst.append(check[i][j])
# print(check_lst)

cnt = 0
result = []
# 체크리스트 한번씩 숫자가 나올때마다 카운트 1씩 증가
for idx in check_lst:
    cnt += 1
    # 해당되는 빙고판의 값을 1로 변경해주기
    for i in range(len(bingo)):
        for j in range(len(bingo[0])):
            if bingo[i][j] == idx:
                bingo[i][j] = 1
    # 이전에 가로 세로 양 대각선의 값이 1일때 카운팅을 해주는 함수 사용
    if finder(bingo) >= 3:
        print(cnt)
        break

