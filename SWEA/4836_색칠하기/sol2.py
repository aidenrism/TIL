import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())
for tc in range(1, T+1):
    n = int(input())

    paper = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(n):
        square = list(map(int, input().split()))

        if square[-1] == 1:

             for i in range(square[0], square[2]+1):
                 for j in range(square[1], square[3]+1):
                     if paper[i][j] == 0 or 2:
                         paper[i][j] += 1

        elif square[-1] == 2:
            for i in range(square[0], square[2] + 1):
                for j in range(square[1], square[3] + 1):
                    if paper[i][j] == 0 or 1:
                        paper[i][j] += 2

    # print(paper)

    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] == 3:
                 cnt += 1

    print('#{} {}'.format(tc ,cnt))
