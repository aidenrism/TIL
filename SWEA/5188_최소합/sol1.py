import sys
sys.stdin = open('input.txt')


# 3. 갈 수 있는 범위인지 확인해주는 함수
def IsSafe(col, row):
    return 0 <= col < n and 0 <= row < n


# 2. 아래 오른쪽을 재귀로 이동 (깊이 우선 탐색)
def BottomRight(col, row):
    global temp

    # 이미 마지막 총합보다 커졌으면 여기까지.. (없으면 시간초과)
    if route[-1] < temp:
        return

    # 마지막값에 도달했다면 그때의 총합을 저장
    if col == n-1 and row == n-1:
        route.append(temp)
        return
    # 하하하 우우우
    for dir in range(2):
        n_col = col + dc[dir]
        n_row = row + dr[dir]
        # 가능한 범위고 아직 안갔더라면 진행
        if IsSafe(n_col, n_row) and (n_col, n_row) not in visited:\
            # 방문체크
            visited.append((n_col, n_row))
            # 그 지점의 값 더하기
            temp += lst[n_col][n_row]
            # 다시 우 하 로 이동하는 함수 실행
            BottomRight(n_col, n_row)
            # 여기까지만 해주면 도착점은 이미 갔던곳이라서 다시 안감
            # 방문한곳과 그 위치의 값들을 삭제
            visited.remove((n_col, n_row))
            temp -= lst[n_col][n_row]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    # 0. 방문여부와 최종합들을 담을 빈 리스트 할당
    visited = []
    route = [9999]
    # 0. 초기값 할당
    temp = lst[0][0]
    # 아래 오른쪽 순으로 이동
    dc = [1, 0]
    dr = [0, 1]
    # 1. 아래 오른쪽으로 돌면서 마지막까지 가는 모든 경로를 구해주는 함수
    BottomRight(0, 0)

    # print(route)
    # print(len(route)) #7,6,9 vs 15 25 51
    # 4. 가본 경로중에 가장 최소값 찾기 (생략)
    # min_route = min(route)
    # min_route = merge_sort(route)[0]
    # print(f'#{tc} {min_route}')

    # 5. 결과값 출력 (가장 마지막 인덱스가 최소값이다)
    print(f'#{tc} {route[-1]}')