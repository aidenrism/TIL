import sys
sys.stdin = open('input.txt')

# 완전이진트리 만들기
def bintree(n):
    global cnt
    # 범위 이내라면 시도
    if n <= N:
        # 왼쪽 자식으로 감
        bintree(n*2)
        # 더 이상 왼쪽으로 못가면 값을 1부터 집어넣는다
        tree[n] = cnt
        cnt += 1
        # 노드에 값을 넣으면 오른쪽으로 자식으로 이동
        bintree(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # print(N)

    tree = [0 for _ in range(N+1)]
    # print(tree)
    cnt = 1
    # 루트 1부터 시작해서 완전이진트리 만들기
    bintree(1)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')


# 중위 순회를 생각하지 못하였다가 하고나니 중위 순회였다는것을 알게 되었다..