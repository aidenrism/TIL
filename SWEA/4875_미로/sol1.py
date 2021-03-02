import sys
sys.stdin = open('input.txt')


def Issafe(col, row):
    return 0 <= col < N and 0 <= row < N and (maze[col][row] == 0 or maze[col][row] == 3)

def dfs(start_c, start_r):
    global result

    # result = 0
    if maze[start_c][start_r] == 3:
        result = 1
        return

    visited.append((start_c, start_r))
    for dir in range(4):
        new_c = start_c + dc[dir]
        new_r = start_r + dr[dir]

        if Issafe(new_c, new_r) and (new_c, new_r) not in visited:
            dfs(new_c, new_r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    for col in range(N):
        for row in range(N):
            if maze[col][row] == 2:
                # print(col, row)
                start_c, start_r = col, row
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    visited = []
    result = 0
    dfs(start_c, start_r)

    print('#{} {}'.format(tc, result))
