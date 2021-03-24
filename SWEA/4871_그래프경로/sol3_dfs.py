import sys
sys.stdin = open('input.txt')

def solution(V, E, graph, S, G):

    visited = [False for _ in range(V+1)]

    def dfs(v):
        visited[v] = True

        for new_v in graph[v]:
            if not visited[new_v]:
                dfs(new_v)
    dfs(S)
    # print(S)
    # return visited
    # print(G) # not E
    return visited[G]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[]for _ in range(V+1)]
    for _ in range(E):
        fr, to = map(int, input().split())
        graph[fr].append(to)
    # print(graph)

    S, G = map(int, input().split())

    print(solution(V, E, graph, S, G))