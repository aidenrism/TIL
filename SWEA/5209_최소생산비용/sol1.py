import sys
sys.stdin = open('input.txt')


# 2. 중복되는 인덱스없이 최소비용을 구하는 함수
def minimum_cost(idx, total):
    global result
    # 이미 구한 값보다 크다면 리턴
    if total > result:
        return
    # 길이만큼 재귀시켰으면 결과를 저장
    if idx == n:
        result = total
    # 길이만큼 돌면서 이 전에 인덱스에 방문안한값들만 재귀
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            minimum_cost(idx+1, total+cost[idx][i])
            # 방문체크 지우기
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    # 0. 방문을 체크하기 위한 리스트
    visited = [0 for _ in range(n)]
    result = 9999
    # 1. 중복되는 인덱스없이 최소비용을 구하는 함수
    minimum_cost(0, 0)

    # 3. 결과값 출력
    print(f'#{tc} {result}')
