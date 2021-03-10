# 시간초과
import sys
sys.stdin = open('input.txt')

def visitable(x, y, direction):
    if direction == RB:
        return x < n and y < n and \
               graph[x - 1][y] == 0 and graph[x][y - 1] == 0 and graph[x][y] == 0

    return x < n and y < n and graph[x][y] == 0


def dfs(loc, direction):
    global answer

    if loc == [n - 1, n - 1]:
        answer += 1

    for next_dir, delta in enumerate(dirs):
        # 45도만 회전시킬 수 있기에, 가로 - 세로, 세로 - 가로는 바로 전환 불가.
        if (direction == B and next_dir == R) or \
                (direction == R and next_dir == B):
            continue

        next_x, next_y = loc[X] + delta[X], loc[Y] + delta[Y]

        if visitable(next_x, next_y, next_dir):
            dfs([next_x, next_y], next_dir)


if __name__ == '__main__':
    X, Y = 0, 1
    R, B, RB = 0, 1, 2
    answer = 0
    dirs = [(0, 1), (1, 0), (1, 1)]
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dfs([0, 1], 0)
    print(answer)