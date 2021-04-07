import sys

sys.stdin = open('input.txt')


# 4. 연산자를 계산해주는 함수
def sol(x):
    n1, n2 = ans.pop(-2), ans.pop()
    # print(ans)
    # print(n1,n2)
    if x == '+':
        n = n1 + n2
    elif x == '-':
        n = n1 - n2
    elif x == '*':
        n = n1 * n2
    else:
        n = n1 / n2
    # print(n)
    ans.append(n)
    # print(ans)


# 3. 후위연산을 위한 함수
def inorder(n):
    # print(ans)
    if n:
        inorder(left[n])
        inorder(right[n])
        # print(node[n])

        # 3-1. 숫자형이면 바로 스택에 삽입
        if type(node[n]) == int:
            ans.append(node[n])
        # 3-2. 연산자 계산해주는 함수로 이동
        else:
            sol(node[n])


# 0.
T = 10
for tc in range(1, 11):
    N = int(input())
    node = [0 for _ in range(N + 1)]
    left = [0 for _ in range(N + 1)]
    right = [0 for _ in range(N + 1)]
    ans = []
    for i in range(N):
        nod = list(input().split())
        # 1. 연산자와 자식노드들이 있는 경우
        if len(nod) == 4:
            n1 = int(nod[0])
            n2 = nod[1]
            n3 = int(nod[2])
            n4 = int(nod[3])
            left[n1] = n3
            right[n1] = n4
        # 2. 숫자만있는 노드
        elif len(nod) == 2:
            n1 = int(nod[0])
            n2 = int(nod[1])
        node[n1] = n2
    # print(node)
    # print(left)
    # print(right)

    # 3. 후위연산을 위한 함수 실행
    inorder(1)
    # print(ans)

    # 5. 대괄호 제거
    ans = int(ans[0])

    print(f'#{tc} {ans}')