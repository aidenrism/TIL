import sys
sys.stdin = open('input.txt')

# stack에서 pop을 하여 인접리스트에 접근한 다음 방문을 표기해주는 함수
def visiting(graph):
    # 시작점
    to_visit = [0]
    # 배열판
    visited = [False for _ in range(100)]

    # print(visited)

    # stack 값이 있는동안 돈다.
    while to_visit:
        # 현재 위치
        corrent = to_visit.pop()
        # 방문기록이 없다면 true로 변경하고 인접리스트의 해당되는 인덱스값을 stack에 append한다
        if not visited[corrent]:
            visited[corrent] = True
            to_visit += graph[corrent]

    return int(visited[99])

for _ in range(10):
    tc, n = map(int, input().split())

    graph = [[] for _ in range(100)]
    load = list(map(int, input().split()))
    start = []
    end = []
    for i in range(len(load)):
        if i%2 == 0:
            start += [load[i]]
        else:
            end += [load[i]]

    for i in range(n):
        graph[start[i]].append(end[i])

    print('#{} {}'.format(tc, visiting(graph)))
    # print(visiting(graph))