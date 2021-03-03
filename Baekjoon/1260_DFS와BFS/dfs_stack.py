import sys
sys.stdin = open('input.txt')

def dfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    path = []

    while to_visits:
        current = to_visits.pop()
        # for idx in to_visits:
        if current not in path:
            # current = True
            path.append(current)
            # print(current)
            to_visits += sorted(G[current])[::-1]
    return path

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v2].append(v1)
    G[v1].append(v2)



print(dfs(V))
# print(G)