import sys
sys.stdin = open('input.txt')

from collections import deque


def is_safe(c, r):
    if 0 <= c < n and 0 <= r < n:
        return 1
    else:
        return 0

def bfs(c, r, idx):
    # 이중리스트로 감싸주어야 아래 node가 리스트 식으로 나와 node[i]에서 c와 r값을 꺼낼 수 있다.
    q = deque([[c, r]])
    # print(q)
    # print(q[0])
    visited[c][r] = 1

    while q:
        node = q.popleft()
        # print(node)
        # print(node[0])
        for dir in range(4):
            nc = node[0] + dc[dir]
            nr = node[1] + dr[dir]
            if is_safe(nc, nr):
                if map[nc][nr] and not visited[nc][nr]:
                    q.append([nc, nr])
                    visited[nc][nr] = 1
                    house[idx] += 1

T =int(input())
n = int(input())
map = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
house = {}
idx = 0
for i in range(n):
    for j in range(n):
        if map[i][j] and visited[i][j] == 0:
            house[idx] = 1
            bfs(i, j, idx)
            idx += 1

# print(house)
# print(house.values())
house = house.values()
# print(house)
print(len(house))
for i in house:
    print(i)
# print(temp)
# house.append(temp)
# temp = 0
