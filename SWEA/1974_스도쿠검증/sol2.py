import sys
sys.stdin = open('input.txt')
def solution(arr):
    for i in range(9):

        h_list_row = []
        h_list_col = []

        for j in range(9):

            if arr[i][j] in h_list_row:
                print(1)
                return 0
            else:
                h_list_row.append(arr[i][j])

            if arr[j][i] in h_list_col:
                print(2)
                return 0
            else:
                h_list_col.append(arr[j][i])

    for i in [0, 3, 6]:

        small_sq1 = []
        small_sq2 = []
        small_sq3 = []

        for j in range(3):

            for k in range(3):
                if arr[i + j][k] in small_sq1:
                    print(3)
                    return 0
                else:
                    small_sq1.append(arr[i + j][k])

            for k in range(3, 6):

                if arr[i + j][k] in small_sq2:
                    print(3)
                    return 0
                else:
                    small_sq2.append(arr[i + j][k])

            for k in range(6, 9):

                if arr[i + j][k] in small_sq3:
                    print(3)
                    return 0
                else:
                    small_sq3.append(arr[i + j][k])

    return 1


T = int(input())

for t in range(1, T + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    print('#{} {}'.format(t, solution(arr)))