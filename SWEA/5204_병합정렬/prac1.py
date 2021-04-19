import sys
sys.stdin = open('input.txt')


def merge_sort(n):
    global cnt
    if len(n) < 2:
        return n
    else:
        mid = len(n)//2
        N = len(n)
        print(mid, N)
        left = n[:mid]
        right = n[mid:N]
        new_lst = []
        print(left, 'left')
        print(right, 'right')
        left = merge_sort(left)
        right = merge_sort(right)

        # 인덱스 처음부터 비교해가면서 더 작은값 새로운 리스트에 더해주기

        l = r = 0
        if left[-1] > right[-1]:
            cnt += 1
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                new_lst.append(left[l])
                l += 1
            else:
                new_lst.append(right[r])
                r += 1

        # 남은거 더해주기
        # if l < len(left):
        #     new_lst.extend(left[l:])
        # else:
        #     new_lst.extend(right[r:])

        # 정렬된 리스트
        # return new_lst
        return new_lst + left[l:] + right[r:]

# def merge_sort(arr):
#     n = len(arr)
#     if n < 2:
#         return arr
#     else:
#         mid = n //2
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

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    cnt = 0
    print(merge_sort(lst))
    print(cnt)