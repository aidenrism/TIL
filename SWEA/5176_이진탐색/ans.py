
def bintree(n):
    global cnt
    if n <= N:
        bintree(n*2)
        tree[n] = cnt
        cnt += 1
        bintree(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    bintree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')