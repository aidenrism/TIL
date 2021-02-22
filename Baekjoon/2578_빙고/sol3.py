import sys
sys.stdin = open('input.txt')

# 빙고판 채우기
# bingo = []
# bingoCheck = [[0 for j in range(5)] for i in range(5)]
# for _ in range(5):
#     bingo.append(input().split())
#
# # 빙고판 체크
# for i in range(5):
#     fiveBingo = input().split()
#     print(fiveBingo)

# data = [(0,0) for i in range(26)]
# print(data)


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


data = [(0, 0) for i in range(26)]
tmp = []
table = [[0 for i in range(5)] for i in range(5)]
idx = 0
call = []
for i in range(5):
    tmp += list((map(int, input().split())))
for i in range(5):
    call += list((map(int, input().split())))

for y in range(5):
    for x in range(5):
        data[tmp[idx]] = (y, x)
        idx += 1

count = 0
call_idx = 0
while call_idx < 12:
    ty, tx = data[call[call_idx]]
    table[ty][tx] = 1
    call_idx += 1
    count += 1

while 1:
    if (finder(table) >= 3):
        print(count)
        break
    ty, tx = data[call[call_idx]]
    table[ty][tx] = 1
    count += 1
    call_idx += 1