import sys
sys.stdin = open('input.txt')

# 3. 대각선 체크 : 같은 대각선상에 있다면 x와 y의 거리의 절대값이 같다 한개라도 안겹치면 True로 반환된다
def check(y, x):
    for i in range(y):
        if y - i == abs(x - diagonal[i]):
            return False
    return True


# 2. n까지 갔을 때 n개의 퀸을 놓는 경우를 세는 함수 실행
def n_queen(y):
    global cnt, result

    # 만약 n까지 갔고 퀸도 n개라면
    if y == n and cnt == n:
        # 경우의 수 더하기
        result += 1
        return

    # row에 x를 넣어가면서 같은 열에 이미 퀸이 있는지 체크
    for x in range(n):
        # 3. 대각선도 체크
        if not visited[x] and check(y, x):
            # 열과 대각선에 체크
            visited[x] = 1
            cnt += 1
            diagonal[y] = x
            # col (y)값 늘리고 재귀
            n_queen(y+1)
            # 재귀후 원상복귀
            visited[x] = 0
            cnt -= 1
            diagonal[y] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())

    # 같은 열과 대각선의 정보를 담을 리스트
    visited = [0 for _ in range(n)]
    diagonal = [0 for _ in range(n)]

    cnt = 0
    result = 0
    # 1. n까지 갔을 때 n개의 퀸을 놓는 경우를 세는 함수 실행
    n_queen(0)

    # 4. 결과값 출력
    print(f'#{tc} {result}')