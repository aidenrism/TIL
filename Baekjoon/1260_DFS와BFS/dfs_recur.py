import sys
sys.stdin = open('input.txt')
def dfs(V):

    to_visits = [V]
    v = to_visits.pop()
    if v not in path:
        path.append(v)
        # new_v = 0

        for new_v in sorted(G[v]):
        # print(sorted(G[v])[0])
            dfs(new_v)

    return path
for tc in range(3):
    N, M, V = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)

    path = []
    print(dfs(V))