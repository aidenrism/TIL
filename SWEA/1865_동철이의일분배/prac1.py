import sys
import time
start = time.time()
sys.stdin = open('input.txt')


def solution(idx, total):
    global result

    if total <= result:
        return
    if idx == n:
        result = total

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            solution(idx+1, total*work[idx][i]*0.01)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # print(n)
    work = [list(map(int, input().split())) for _ in range(n)]
    # print(work)
    result = 0
    visited = [0 for _ in range(n)]
    solution(0, 1)

    result = result*100
    # print(result)
    print(f'#{tc} {result:.6f}')
print("time :", time.time() - start)