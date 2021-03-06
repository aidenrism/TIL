import sys
sys.stdin = open('input.txt')

# 사각형의 크기를 찾아주는 함수
def search_size(r,c):
    r_cnt = 0
    c_cnt = 0

    # 행의 길이를 찾는
    for i in range(r, N):
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break
    # 열의 길이를 찾는
    for i in range(c, N):
        if arr[r][i] != 0:
            c_cnt += 1
        else:
            break

    ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
    init(r, c, r_cnt, c_cnt)

# 화학물질을 빈용기로 변환
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r_cnt):
        for j in range(c, c_cnt):
            arr[i][j] = 0

def counting_sort(idx): # 첫번째 기준으로 정렬할거냐 두번째 변수를 기준으로 정렬할거냐
    cnt = [0] * 10001
    sort_ans = [0] * len(ans)

    # 1. 카운팅 하는 과정
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1

    # 2. 누적
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    # 3. 정렬하여 넣는 과정
    for i in range(len(ans)-1, -1, -1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1

    return sort_ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    ans = []

    # 행우선순회 방식으로 순회하면서 사각형의 시작좌표를 구한다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0
                search_size(i,j)

    ans = counting_sort(0) # 행을 기준으로 정렬
    ans = counting_sort(2) # 행렬의 크기로 다시한번 정렬

    print('#{} {}'.format(tc, len(ans)), end= ' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end= ' ')
    print()

################################################################

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                #범위를 앞에 위치
                while c < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1

                ans.append([r-i, c-j])

                # 초기화 하는 과정
                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0

    # 첫번째 곱한값을 기준으로 정렬하고 안되면 다음값을 기준으로 정렬
    ans.sort(key = lambda x : (x[0]*x[1], x[0]))
    print('#{} {}'.format(tc, len(ans)), end= ' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end= ' ')
    print()