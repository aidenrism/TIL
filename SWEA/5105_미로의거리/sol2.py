## x
import sys
sys.stdin = open('input.txt')

def Issafe(y,x):

    return N > x >= 0 and N > y >= 0

def bfs(maze):
    # 상하좌우
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    current = (col, row)

    visited = [[current] for _ in range(4)]

    to_visits = [current]
    cnt = 0
    while to_visits:
        current = to_visits.pop()
        for dir in range(4):
            n_col = current[0] + dc[dir]
            n_row = current[1] + dr[dir]

            if Issafe(n_col,n_row) and maze[n_col][n_row] == 0 :

                if (n_col, n_row) not in visited[dir]:
                    visited[dir].append((n_col, n_row))
                    to_visits.append((n_col, n_row))

            elif Issafe(n_col,n_row) and maze[n_col][n_row] == 3:
                cnt += 1
                if (n_col, n_row) not in visited:
                    visited.append((n_col, n_row))
                    print(visited)
                    print(len(visited),'ww')
                    # return abs(n_col - col) + abs(n_row - row) - 1



    # print(cnt)
    # return 0
    print(len(visited),'xx')
    print(visited)
    # emp = [[0] * N for _ in range(N)]
    # print(emp)


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