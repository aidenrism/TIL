import time
import sys
sys.stdin = open('input.txt')

start = time.time()

# 2. 가장 높은 확률 구해주는 함수
def solution(idx, total):
    global result

    # 이미 크거나 같다면 끝내주기 (같다를 주지 않으면 36번 테케에서 안 끝남)
    if total <= result:
        return
    # 사람수만큼 왔다면 결과값 저장
    if idx == n:
        result = total

    # 사람한명이 한명의 일을 가져가게 기록체크 재귀하고나선 기록 지우기
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
    # 1. 가장 높은 확률을 구해주는 함수 (곱셈이니 두번째 인덱스 total은 1)
    solution(0, 1)
    result = result*100

    # 3. 결과값 출력
    print(f'#{tc} {result:.6f}')
print("time :", time.time() - start)