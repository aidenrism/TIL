import sys
sys.stdin = open('input.txt')

# testcase값 입력
for tc in range(1, int(input())+ 1):
    # 정사각형의 한 변의 길이
    n = int(input())

    snail = [[0 for _ in range(n)] for _ in range(n)]
    # print(snail)

    # 넣을 숫자
    num = 1
    # 초기 세로 가로 값
    col, row = 0, -1
    # 좌하 우하 이동할때 col과 row에 방향을 바꿔줌
    step = 1

    while n > 0:
        for _ in range(n):
            row += 1 * step
            snail[col][row] += num
            num += 1
        # n값을 하나씩 줄여줌
        n -= 1
        for _ in range(n):
            col += 1 * step
            snail[col][row] += num
            num += 1
        #col row 방향 변경
        step *= -1

    print('#{}'.format(tc))
    for i in range(len(snail)):
        print(*snail[i])