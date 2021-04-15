import sys
sys.stdin = open('input.txt')


# 3. 머지소트(병합정렬)
def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        mid = n //2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        new_arr = []
        l = r = 0
        while l < mid and r < n - mid:
            if left[l] < right[r]:
                new_arr.append(left[l])
                l += 1
            else:
                new_arr.append(right[r])
                r += 1
        return new_arr + left[l:] + right[r:]


# 2. 만든 순열을 사용해 해당 위치의 값 더해주기
def GolfArea(arr):
    # 첫번째 값과 마지막값은 초기에 넣어줌
    temp = area[0][arr[0]] + area[arr[-1]][0]
    # 순열 돌린거 집어넣으며 임시변수에 더해주기
    for i in range(len(arr)-1):
        temp += area[arr[i]][arr[i+1]]
    # 총합 리스트
    total.append(temp)


# 1. 순열만들기
def perm(idx, length):
    # 전체 길이만큼 왔으면 해당 위치의 값을 더해주는 함수 실행
    if idx == length:
        # print(arr)
        GolfArea(arr)
    # 자리를 바꿔주며 순열을 만듦
    else:
        for change in range(idx, length):
            arr[idx], arr[change] = arr[change], arr[idx]
            perm(idx+1, length)
            arr[idx], arr[change] = arr[change], arr[idx]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 2차원리스트의 골프장
    area = [list(map(int, input().split())) for _ in range(n)]
    # 0. 첫번째 값을 제외하고 순열 고고
    arr = [i for i in range(1, n)]
    # 0. 배터리 소비량의 총합을 담을 리스트
    total = []
    # 1. 순열돌리는 함수 실행
    perm(0, n-1)

    # 3. 병합정렬후 가장 작은 최소값 저장
    min_total = merge_sort(total)[0]
    # 4. 결과값 출력
    print(f'#{tc} {min_total}')