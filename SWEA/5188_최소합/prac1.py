import sys
sys.stdin = open('input.txt')


def IsSafe(col, row):
    return 0 <= col < n and 0 <= row < n


def bottomright(col, row):
    global temp

    if col == n-1 and row == n-1:
        route.append(temp)

    for dir in range(2):
        n_col = col + dc[dir]
        n_row = row + dr[dir]
        if IsSafe(n_col, n_row) and (n_col, n_row) not in visted:
            visted.append((n_col, n_row))
            temp += lst[n_col][n_row]
            bottomright(n_col, n_row)
            # 여기까지만 해주면 도착점은 이미 갔던곳이라서 다시 안감
            # 방문한곳과 그 위치의 값들을 삭제
            visted.remove((n_col, n_row))
            temp -= lst[n_col][n_row]


    # visited 를 체크해주면 안된다 (갔던대로 또 가볼 수 있어야 함)--간 부분만 제거해주면 됨
    # if col < n and row < n and (col, row) not in visted:
    #     route.append(lst[col][row])
    #     visted.append((col, row))
    #     bottomright(col+1, row)
    #     bottomright(col, row+1)
    #     bottomright(col+1, row)
    # else:
    #     return
    # # bottomright(col, row)

n = int(input())
print(n)
lst = [list(map(int, input().split())) for _ in range(n)]
print(lst)
visted = []
route = []
temp = lst[0][0]
# 아래 오른쪽
dc = [1, 0]
dr = [0, 1]
bottomright(0, 0)
print(visted)
print(route)
print(temp)
min_route = min(route)
print(min_route)



## 2

# def merge_sort(arr):
#     n = len(arr)
#     if n < 2:
#         return arr
#     else:
#         mid = n // 2
#         left = merge_sort(arr[:mid])
#         right = merge_sort(arr[mid:])
#         new_arr = []
#         l = r = 0
#         while l < mid and r < n - mid:
#             if left[l] < right[r]:
#                 new_arr.append(left[l])
#                 l += 1
#             else:
#                 new_arr.append(right[r])
#                 r += 1
#         return new_arr + left[l:] + right[r:]
# 3. 갈 수 있는 범위인지 확인해주는 함수
def IsSafe(col, row):
    return 0 <= col < n and 0 <= row < n


# 2. 아래 오르쪽을 재귀로 이동 (깊이 우선 탐색)
def BottomRight(col, row):
    global temp

    # if route[-1] < temp:
    #     return

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

    print(route)
    print(len(route)) #7,6,9 vs 15 25 51
    # 4. 가본 경로중에 가장 최소값 찾기
    # min_route = min(route)
    # min_route = merge_sort(route)[0]
    # print(f'#{tc} {min_route}')
    print(f'#{tc} {route[-1]}')