import sys
sys.stdin = open('input.txt')

def Issafe(y,x):
    return 0 < y < 16 and 0 < x < 16 and (maze[y][x] == 0 or maze[y][x] == 3)

def dfs(y,x):
    visited = []
    to_visits = []
    to_visits.append((st_y, st_x))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while to_visits:
        y, x = to_visits.pop()
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]

            if Issafe(new_y, new_x) and (new_y, new_x) not in visited:
                visited.append((new_y, new_x))
                to_visits.append((new_y, new_x))

            if (new_y, new_x) == (end_y, end_x):
                return 1
    return 0


for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    st_y, st_x = 1, 1
    end_y, end_x = 13, 13

    print('#{} {}'.format(T, dfs(st_y,st_x)))