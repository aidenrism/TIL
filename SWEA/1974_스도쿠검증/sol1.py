import sys
sys.stdin = open('input.txt')

def Isreal(sudoku):
    cnt1 = 0
    cnt2 = 0
    result = 0
    for i in range(9):
        cnt1 = 0
        cnt2 = 0

        for j in range(9):
            cnt1 += sudoku[i][j]
            cnt2 += sudoku[j][i]
            cnt3 = 0
            if (i % 3 == 0 and j % 3 == 0):
                for k in range(3):
                    for l in range(3):

                        cnt3 += sudoku[i + k][j + l]
                if cnt3 != 45:
                    result += 1
        if (cnt1 != 45 or cnt2 != 45):
            # if (cnt1 and cnt2) != 45:
            # if cnt1 != 45 and cnt2 != 45:
            result += 1
    if result == 0:
        return 1
    else:
        return 0


    # print(cnt1)
    # print(cnt2)
    # print(cnt3)

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, Isreal(sudoku)))
