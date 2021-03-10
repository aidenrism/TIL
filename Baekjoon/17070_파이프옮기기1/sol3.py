# dp는 다시 학습하자
import sys
sys.stdin = open('input.txt')

if __name__ == '__main__':
    R, B, RB = 0, 1, 2
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    # [x][y][direction]
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

    # 시작 위치 1로 초기화
    dp[0][1][R] = 1

    for y in range(2, n):
        if graph[0][y] == 0:
            dp[0][y][R] = dp[0][y - 1][R]

    for x in range(n):
        for y in range(2, n):
            # 대각선으로 이동하기 위해서는 가로, 세로, 대각선이 벽이 아니어야 함.
            if graph[x][y] == graph[x][y - 1] == graph[x - 1][y] == 0:
                dp[x][y][RB] = \
                    dp[x - 1][y - 1][R] + dp[x - 1][y - 1][B] + dp[x - 1][y - 1][RB]

            if graph[x][y] == 0:
                dp[x][y][R] = dp[x][y - 1][R] + dp[x][y - 1][RB]
                dp[x][y][B] = dp[x - 1][y][B] + dp[x - 1][y][RB]

    print(sum(dp[-1][-1]))