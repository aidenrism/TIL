import sys
sys.stdin = open('input.txt')


# 3. 해당 위치를 포함해 더해가면서 7개가 되면 셋에 더해주는 함수 실행
def make_seven(n, c, r):
        global unique
        if len(n) == 7:
            # 셋 함수에 더하기
            unique.add(n)
            return
        # 델타이동을 해주며 사방면 탐색
        for dir in range(4):
            n_col, n_row = c + dc[dir], r + dr[dir]
            # 지정된 범위 내에서라면 실행
            if 0 <= n_col < 4 and 0 <= n_row < 4:
                make_seven(n+grid[n_col][n_row], n_col, n_row)


T = int(input())
for tc in range(1, T+1):
    # 0. 이차원 리스트
    grid = [list(input().split()) for _ in range(4)]
    # print(grid)
    # 1. set함수로 중복을 막아준다.
    unique = set()
    dc = (0, 0, -1, 1)
    dr = (-1, 1, 0, 0)
    # 2. 모든 곳을 한번씩 방문하여준다.
    for c in range(4):
        for r in range(4):
            # 3. 해당 위치를 포함해 더해가면서 7개가 되면 셋에 더해주는 함수 실행
            make_seven(grid[c][r], c, r)
    # 4. 결과값 출력
    print(f'#{tc} {len(unique)}')




# set을 쓰지 않으면 시간 10배 더 걸림

#
# def make_seven(n, c, r):
#     global route
#     # route += grid[c][r]
#     if len(n) == 7:
#         if n not in emp:
#             emp.append(n)
#         return None
#     for dir in range(4):
#         n_col, n_row = c + dc[dir], r + dr[dir]
#         if 0 <= n_col < 4 and 0 <= n_row < 4:
#             make_seven(n + grid[n_col][n_row], n_col, n_row)
#             # route = route[::-1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     grid = [list(input().split()) for _ in range(4)]
#     # print(grid)
#     emp = []
#     route = ''
#     # unique = set()
#     dc = (0, 0, -1, 1)
#     dr = (-1, 1, 0, 0)
#     for c in range(4):
#         for r in range(4):
#             make_seven(grid[c][r], c, r)
#
#     print(f'#{tc} {len(emp)}') #16488