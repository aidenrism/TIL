from heapq import heappop, heappush

# 10개중 8개 성공
import sys
sys.stdin = open('input.txt')


# 2. 다익스트라 함수 실행
def dijkstra(s, d):
    global gragh
    n = len(gragh)
    table = [INF for i in range(n)]
    table[s] = 0
    pq = [[0, s]]

    while pq:
        w, x = heappop(pq)

        if table[x] < w:
            continue

        for item in gragh[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            if ncost < table[nx]:
                table[nx] = ncost
                heappush(pq, [ncost, nx])

    return table[d]


T = int(input())
for tc in range(1, T+1):
    n, e = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(e)]
    INF = int(1e9)

    # 1. 주어진 s, e, w 를 이용하여 그래프를 그립니다
    gragh = [[] for _ in range(n+1)]
    for node in nodes:
        st, ed, le = node[0], node[1], node[2]
        gragh[st].append([ed, le])
        gragh[ed].append([st, le])
    # print(gragh)

    # 2. 다익스트라 0부터 n까지 거리를 구해줍니다.

    # 3. 결과값 출력
    dist = dijkstra(0, n)
    for i in range(1, n):
        dist = min(dist, dijkstra(0, i) + dijkstra(i, n))

    print(f'#{tc} {dist}')

