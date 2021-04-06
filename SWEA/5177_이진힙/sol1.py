import sys
sys.stdin = open('input.txt')


# 3. 부모노드가 자식노드보다 클 때 두 노드의 위치를 바꾸기
def change(n):
    if node[n] < node[n//2]:
        node[n//2], node[n] = node[n], node[n//2]
        # 이 코드를 넣지 않으면 tc 3개만 통과
        change(n//2)

# 4. 조상노드들의 값을 모두 더해주기
def solve(n):
    cnt = 0
    while n > 0:
        cnt += node[n//2]
        # 조상노드로 또 가기
        n //= 2
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = list(map(int, input().split()))
    # 1. 첫번째 인덱스에 0 추가
    node.insert(0, 0)
    # print(node)

    # 2. 인덱스 1일때는 0과 바꾸면 안되므로 높이 2에서부터 change함수 시작
    for i in range(len(node)):
       if i >= 2:
           change(i)

    # print(node)
    # 5. 결과값 출력
    print(f'#{tc} {solve(N)}')


