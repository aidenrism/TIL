from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(idx):
    global cnt

    q = deque()
    q.append((idx,0))
    check = {}

    while q:
        x, cnt = q.popleft()
        # if x > 1000000:
        #     return

        if check.get(x):
            continue
        check[x] = 1
        if x == b:
            return cnt
        cnt += 1
        # q.append(x+1)
        # q.append(x-1)
        # q.append(x*2)
        # q.append(x-10)
        if 0 < x + 1 <= 1000000:
            q.append((x+1, cnt))
        if 0 < x - 1 <= 1000000:
            q.append((x-1, cnt))
        if 0 < x * 2 <= 1000000:
            q.append((x*2, cnt))
        if 0 < x - 10 <= 1000000:
            q.append((x-10, cnt))

T = int(input())
a, b = map(int, input().split())
cnt = 0
bfs(a)
print(cnt)