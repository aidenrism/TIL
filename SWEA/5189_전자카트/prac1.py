import sys
sys.stdin = open('input.txt')

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

# 만든 순열을 사용해 해당 위치의 값 더해주기
def GolfArea(arr):
    temp = area[0][arr[0]] + area[arr[-1]][0]
    for i in range(len(arr)-1):
        temp += area[arr[i]][arr[i+1]]
        # print(temp)
    total.append(temp)

# 순열만들기
def perm(idx, length):
    if idx == length:
        # print(arr)
        GolfArea(arr)
    else:
        for change in range(idx, length):
            arr[idx], arr[change] = arr[change], arr[idx]
            perm(idx+1, length)
            arr[idx], arr[change] = arr[change], arr[idx]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    # print(area)
    arr = [i for i in range(1, n)]
    total = []
    perm(0, n-1)
    # print(merge_sort(total))
    min_total = merge_sort(total)[0]
    print(f'#{tc} {min_total}')
    # (perm(0,3)
    # n = 4
    # arr = [i for i in range(1, n)]
    # print(arr)