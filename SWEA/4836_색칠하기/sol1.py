import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())
for tc in range(1, T+1):
    # 사각형의 개수 입력
    n = int(input())
    # 백지 생성
    paper = [[0] * 10 for _ in range(10)]
    # cnt = 0
    for num in range(n):
        square_num = list(map(int, input().split()))
        # 빨강색에 해당되는 인덱스는 백지에 1로 표시
        if square_num[-1] == 1:
            # color = 'red'
            for i in range(square_num[0], square_num[2] + 1):
                for j in range(square_num[1], square_num[3] + 1):
                    if paper[i][j] == 0:
                        paper[i][j] = 1
                    elif paper[i][j] == 2:
                        paper[i][j] = 3
                    # elif paper[i][j] == 3:
                    #     paper[i][j] = 4

        # 파란색은 빨강색이 있을 때 1을 더해준다
        elif square_num[-1] == 2:
            # color = 'blue'
            for i in range(square_num[0], square_num[2] + 1):
                for j in range(square_num[1], square_num[3] + 1):
                    if paper[i][j] == 1:
                        paper[i][j] = 3
                    elif paper[i][j] == 0:
                        paper[i][j] = 2
                    # elif paper[i][j] == 3:
                    #     paper[i][j] = 4
                # print(i, j)
        # print(color)
        # 2인거의 개수를 세기
        # cnt = 0 # cnt를 여기서 초기화해주지않고 위에서 초기화해서 계속 실패하였다..
        for i in range(len(paper)):
            for j in range(len(paper)):
                if paper[i][j] == 3:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))
