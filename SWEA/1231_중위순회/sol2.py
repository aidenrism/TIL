import sys
sys.stdin = open('input.txt')


## 전위순회 VLR 루트 -> 레프트 -> 라이트
def preorder(n):
    if int(n) > 0:
        print(word[int(n)], end=' ')
        preorder(left[int(n)])
        preorder(right[int(n)])


## 중위순회 LVR 레프트 -> 루트 -> 라이트
def inorder(n):
    if int(n) > 0:
        inorder(left[int(n)])
        print(word[int(n)], end=' ')
        inorder(right[int(n)])

## 후위순회 LRV 레프트 -> 라이트 -> 루트
def postorder(n):
    if int(n) > 0:
        postorder(left[int(n)])
        postorder(right[int(n)])
        print(word[int(n)], end=' ')

T = 1

for tc in range(T):

    V = int(input())
    left = [0]*(V+1)
    right = [0]*(V+1)
    word = [0]*(V+1)


    for i in range(V):
        N = list(input().split())
        # print(N)
        # 단어 그래프를 만들어줌
        word[int(N[0])] = N[1]
        if len(N) == 4:
            # 네번째 값까지 있다면 양쪽에 넣어줌
            left[int(N[0])] = N[2]
            right[int(N[0])] = N[3]

        if len(N) == 3:
            # 길이가 3이라면 왼쪽에 넣어줌
            left[int(N[0])] = N[2]

    # print(word)
    # print(left)
    # print(right)

    # preorder(1)
    # print()
    inorder(1)
    # print()
    # postorder(1)
    # if left[N[0]] == 0:
    #     left[N[0]] = left[N[2]]
    # else:
    #     left[N[0]] = left[N[3]]
