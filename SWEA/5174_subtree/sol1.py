# 3. 해당 노드의 아래 있는 노드들을 탐색하고 그때마다 1씩 더해준다.
def order(n):
    global cnt

    if tree[0][n] != 0:
        num = tree[0][n]
        cnt += 1
        order(num)
    if tree[1][n] != 0:
        num = tree[1][n]
        cnt += 1
        order(num)
    return cnt


T = int(input())
for tc in range(1, T + 1):
    n, num = map(int, input().split())
    node = list(map(int, input().split()))
    # print(node)
    # print(max(node))
    tree = [[0] * (n + 2) for _ in range(2)]
    # print(tree)

    # 1. 2개마다 앞에 값을 인덱스 뒤에값을 해당 인덱스 위치의 값으로 넣는다
    for i in range(n * 2):
        if i % 2 == 0:
            n1, n2 = node[i], node[i + 1]
            # 2-1. 왼쪽 자식이 없으면 왼쪽부터
            if tree[0][n1] == 0:
                tree[0][n1] = n2
            # 2-2. 있으면 오른쪽도
            else:
                tree[1][n1] = n2

    # print(tree)
    cnt = 1
    print('#{} {}'.format(tc, order(num)))


