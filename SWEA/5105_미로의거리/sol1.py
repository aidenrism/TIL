import sys
sys.stdin = open('input.txt')

def Issafe(y,x):

    return N > x >= 0 and N > y >= 0

def bfs(maze):
    # 상하좌우
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    current = (col, row)
    visited = [current]
    to_visits = [current]
    distance = [[0]* N for _ in range(N)]

    while to_visits:
        current = to_visits.pop(0)
        for dir in range(4):
            n_col = current[0] + dc[dir]
            n_row = current[1] + dr[dir]

            if Issafe(n_col,n_row) and maze[n_col][n_row] == 0 :

                if (n_col, n_row) not in visited:
                    visited.append((n_col, n_row))
                    to_visits.append((n_col, n_row))
                    distance[n_col][n_row] = distance[current[0]][current[1]] + 1

            elif Issafe(n_col,n_row) and maze[n_col][n_row] == 3:
                return distance[current[0]][current[1]]

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                col, row = i, j

    print('#{} {}'.format(tc, bfs(maze)))