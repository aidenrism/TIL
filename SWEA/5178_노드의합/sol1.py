import sys
sys.stdin = open('input.txt')


def add(n):
    if n > 1:
        node[n//2] += node[n]
        # 4. 이미 왼쪽 자식에게 더해진 노드는 오른쪽 자식노드에게 더해질 때
        # 그 위 부모노드에 더한값 반영하기
        if node[n//2] != node[n]:
            add(n//2)
        # 5. 마지막 노드가 외자식이라면 얘는 바로 더해준다.
        elif n == N:
            add(n//2)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 1. 빈 노드 값 리스트 만들기
    node = [0 for _ in range(N+1)]
    # 2. 리프 노드들 값을 각 자리에 넣어주기
    for i in range(M):
        n1, n2 = map(int, input().split())
        node[n1] = n2
        # 3. 부모노드들에게 자식노드의 값을 더해주는 함수
        add(n1)
    # print(node)
    print(f'#{tc} {node[L]}')
