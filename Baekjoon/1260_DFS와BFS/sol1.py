import sys
sys.stdin = open('input.txt')

def dfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    path = []

    # 스택에 쌓인 값들이 있는 동안 반복
    while to_visits:
        # 뒤쪽에서부터 추출
        current = to_visits.pop()
        # for idx in to_visits:
        if current not in path:
            # current = True
            path.append(current)
            # print(current)
            # 작은 값들부터 확인한다고 문제에서 나왔으므로 정렬후 4321 로 해야 마지막 인덱스인 1으로 뻗어나간다.
            to_visits += sorted(G[current])[::-1]
    return path

def bfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    path = []

    while to_visits:
        # for _ in range(len(to_visits)):
        # 처음 시작점에서부터 인접한 값들부터 방문할 것이므로 첫값에서 append된 앞쪽부터 살펴본다
        # 이 값들에서 나온 값들은 뒤에 append되므로 나중에 방문하지 못하였을시 방문하게된다.
         current = to_visits.pop(0)
        # for idx in to_visits:
         if current not in path:
            # current = True
            path.append(current)
            # print(current)
            # pop을 앞에서 부터 하고 작은값부터 문제에서 방문하기로 하였으므로 오름차순 정렬
            to_visits += sorted(G[current])
    return path

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v2].append(v1)
    G[v1].append(v2)

print(*dfs(V))
print(*bfs(V))