import sys
sys.stdin = open('input.txt')
#
#
# # def solution(n):
# #     for
#
# n, m = map(int, input().split())
# inf = 99999
# graph = [[inf for _ in range(n+1)] for _ in range(n+1)]
# for _ in range(m):
#     st, ed, w =
#     graph[st][ed] = w
#     graph[ed][st] = w
# print(graph)
#
#
# for i in range(n+1):
#     for j in range(n+1):
#         if i != 1 and graph[1][i] > graph[1][j] + graph[j][i]:
#             graph[1][i] = graph[1][j] + graph[j][i]
#             print(i,j)
#
# print(graph)
# # solution(1)

import sys
from heapq import heappush, heappop

def Dijkstra(K, graph, V):
    heap = []
    distance = [1e9] * (V + 1)
    distance[K] = 0
    cource = [0] * (V + 1)
    heappush(heap, (0, K))

    while heap:
        weight, location = heappop(heap)

        if distance[location] < weight:
            continue

        for l, w in graph[location]:
            w += weight
            if w < distance[l]:
                distance[l] = w
                cource[l] = location
                heappush(heap, (w, l))
    return cource

def solution():
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append([v, w])
        graph[v].append([u, w])

    for idx in range(1, V+1):
        course = Dijkstra(idx, graph, V)
        ret = ['-'] * (V + 1)
        for jdx in range(1, V+1):
            if idx == jdx:
                continue
            checkIndex = jdx
            while 1:
                kdx = course[checkIndex]
                if kdx == idx:
                    ret[jdx] = checkIndex
                    break
                checkIndex = kdx
        for i in range(1, V+1):
            print(ret[i], end=' ')
        print()

solution()