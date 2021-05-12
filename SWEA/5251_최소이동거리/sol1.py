from heapq import heappop, heappush

# 10개중 8개 성공
import sys
sys.stdin = open('input.txt')


# 2. 다익스트라 함수 실행
def dijkstra(s, d):
    global gragh, a
    # n = len(gragh)
    table = [INF for i in range(n+1)]
    table[s] = 0
    pq = [(0, 0)]
    visited = [0 for _ in range(n+1)]
    # print(gragh)
    while pq:
        d, idx = heappop(pq)

        if visited[idx]:
            continue

        visited[idx] = 1
        for a, b in gragh[idx]:
            if b + d < table[a]:
                table[a] = b + d
                heappush(pq, [table[a], a])

    return table[a]


T = int(input())
for tc in range(1, T+1):
    n, e = map(int, input().split())
    # nodes = [list(map(int, input().split())) for _ in range(e)]
    # node = [[] for _ in range(n + 1)]
    INF = int(1e9)

    # 1. 주어진 s, e, w 를 이용하여 그래프를 그립니다
    gragh = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = list(map(int, input().split()))
        gragh[a].append((b, c))
    # print(gragh)

    # 2. 다익스트라 0부터 n까지 거리를 구해줍니다.

    # 3. 결과값 출력
    dist = dijkstra(0, n)
    # for i in range(1, n):
    #     dist = min(dist, dijkstra(0, i) + dijkstra(i, n))

    print(f'#{tc} {dist}')

