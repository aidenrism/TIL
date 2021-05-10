from collections import deque
import sys

sys.stdin = open('input.txt')


# 2. bfs를 돌며 a에서 b만드는 연산
def bfs(a, b):
    global cnt
    q = deque()
    # 초기값, cnt를 같이 넘겨주지 않으면 한 단계의 bfs에서 카운팅을 저장하지 못함.. 숫자하나하나마다 카운팅누적
    q.append((a, 0))
    # 중복을 제거할 딕셔너리
    check = {}

    while q:
        num, cnt = q.popleft()
        # tc 3개-> 6개 이미 벨류가 있는 num 이라면 다음 회차 while q로 넘어간다.
        if check.get(num):
            continue
        check[num] = 1
        if num == b:
            return cnt
        cnt += 1
        # 백만 넘게까지 주면 tc를 모두 통과하지 못함
        if 0 < num + 1 <= 1000000:
            q.append((num+1, cnt))
        if 0 < num - 1 <= 1000000:
            q.append((num-1, cnt))
        if 0 < num * 2 <= 1000000:
            q.append((num*2, cnt))
        if 0 < num - 10 <= 1000000:
            q.append((num-10, cnt))




T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    cnt = 0
    # 1. bfs를 돌며 b값이 되게 연산
    bfs(a, b)
    # 3. 결과값출력
    print(f'#{tc} {cnt}')