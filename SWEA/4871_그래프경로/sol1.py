import sys
sys.stdin = open('input.txt')

def visiting(v, graph, S, G):

    # 값들을 stack할 리스트 초기값은 출발점을 준다
    to_visit = [S]

    # 값들의 방문 여부를 확인할 리스트 (숫자를 그대로 인덱스 값으로 받으려면 노드값에 1을 더해주면 됨
    visited = [False for _ in range(v+1)]

    # 스택에 값이 있는동안 반복한다.
    while to_visit:
        # 현재 위치는 스택에서 나온값
        current = to_visit.pop()
        # 방문하지 않았다면 T로 체크해주고 거기에 해당되는 인접리스트를 스택에 append 시킨다.
        # if visited[current] == False: # 밑에와 같음
        if not visited[current]:
            visited[current] = True
            # append는 [3,4]를 리스트로 해준다 3,4만 들어가게 해줘야 에러가 안남.
            to_visit += graph[current]

    # goal의 값이 방문이 되었는지 체크하고 결과로 반환한다. true false를 숫자로 변환
    return int(visited[G])



T = int(input())

for tc in range(1, T+1):
    # 버텍스(노드)와 엣지
    v, e = map(int, input().split())
    # print(v,e)
    # 2차원 인접리스트의 생성  (연결이 시작되는 노드를 인덱스 값으로 주고 거기에서 이어지는 노드를 2차원리스트에 삽입한다.)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        fr, to = map(int, input().split())
        graph[fr].append(to)

    # 스타트와 골
    S, G = map(int, input().split())

    # print(graph)
    print('#{} {}'.format(tc, visiting(v, graph, S, G)))
