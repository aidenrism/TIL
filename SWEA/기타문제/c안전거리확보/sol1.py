import sys
sys.stdin = open('input.txt')

# 범위이내인지 확인 
def Issafe(y, x):
    return 0 < y < n and 0 < x < n and room[y][x] == '0'

# 노마스크가 확산 가능한지 확인 
def dfs(y, x):
    visited = []
    to_visit = []
    to_visit.append((st_y, st_x))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while to_visit:
        y, x = to_visit.pop()
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]

            if Issafe(new_y, new_x) and (new_y, new_x) not in visited:
                visited.append((new_y, new_x))
                to_visit.append((new_y, new_x))

                if room[new_y][new_x] == 'M':
                    return 1
    return 0

# 마스크끼리 2이상 거리가 되는지 확인 
def bfs(y, x):
    visited = []
    to_visit = []
    to_visit.append((st_y, st_x))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while to_visit:
        y, x = to_visit.pop(0)
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]

            if Issafe(new_y, new_x) and (new_y, new_x) not in visited:
                visited.append((new_y, new_x))
                to_visit.append((new_y, new_x))
                distance[new_y][new_x] = distance[st_y][st_x] +1
                # print(distance[new_y][new_x], distance)
                # print(st_y,st_x)
                if distance[new_y][new_x] > 2:
                    return 0
                if room[new_y][new_x] == 'M':
                    return 1
    return 0

# 0. 
T = int(input())
n = int(input())

room = list(input().split() for _ in range(n))

# 0-1. 거리확인을 위한 빈 리스트
distance = [[0]*n for _ in range(n)]
result = 0 

# 1. dfs와 bfs로 노마스크와 마스크의 안전 여부 확인 
for i in range(n):
    for j in range(n):
        if room[i][j] == 'N':
            # print(f'room {i,j} 노마스크')
            st_y, st_x = i, j
            if dfs(st_y, st_x):
                result += 1

        if room[i][j] == 'M':
            st_y, st_x = i, j
            if bfs(st_y, st_x):
                result += 1

# 2. 하나라도 안전하지 않았다면 완전하지 않다는 출력값 주기 
if result != 0:
    print('No') # 안전 x
else:
    print('Yes') # 안전
    
