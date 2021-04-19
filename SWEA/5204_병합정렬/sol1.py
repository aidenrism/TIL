import sys
sys.stdin = open('input.txt')


# 1. 병합정렬로 정렬된 리스트만들기
def merge_sort(n):
    global cnt
    # 1-1. 길이가 2보다 작다면 그 값을 반환
    if len(n) < 2:
        return n
    # 1-2. 길이가 2이상이라면 2보다 작을 때 까지 반으로 나눈다
    else:
        mid = len(n)//2
        N = len(n)
        left = n[:mid]
        right = n[mid:N]
        new_lst = []
        # 마지막까지 반으로 나누기
        left = merge_sort(left)
        right = merge_sort(right)

        # 1-3. 나눈값들을 인덱스 처음부터 비교해가면서 더 작은값 새로운 리스트에 더해주기
        l = r = 0
        # 1-4. 나눈값중에 왼쪽 끝값이 더 크다면 cnt로 세어주기
        if left[-1] > right[-1]:
            cnt += 1
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                new_lst.append(left[l])
                l += 1
            else:
                new_lst.append(right[r])
                r += 1

        # 1-5. 남은거 더해주기
        if l < len(left):
            new_lst.extend(left[l:])
        else:
            new_lst.extend(right[r:])

        # 1-6. 정렬된 리스트를 차례로 반환
        return new_lst
        # return new_lst + left[l:] + right[r:]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    # 1. 병합정렬로 정렬된 리스트만들기
    merge_lst = merge_sort(lst)

    # print(cnt)
    # lst[len(lst)//2]

    # 2. 병합정렬로 정렬된 리스트의 중간값
    mid_num = merge_lst[len(lst)//2]

    # 3. 결과값 출력
    print(f'#{tc} {mid_num} {cnt}')
