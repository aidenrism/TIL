import sys
sys.stdin = open('input.txt')


# 2. 이진탐색 함수
def binary_search(lst, num):
    # 초기값들
    left = 0
    right = n-1

    # is_left = False
    # is_right = False
    lr_check = 0

    result = 0
    # 둘이 만나기 전까지 반복
    while left <= right:
        mid = (left+right)//2
        # m값이라면 찾았으니 1을 반환
        if A[mid] == num:
            result = 1
            return result
        # 원소가 m보다 작다면 오른쪽을 이동시켜 left로 체크
        elif A[mid] > num:
            if lr_check == -1:
                return result
            # is_left = True
            lr_check = -1
            right = mid - 1


        # 원소가 m보다 크다면 왼쪽을 이동시켜 right 체크
        elif A[mid] < num:
            if lr_check == 1:
                return result
            # is_right = True
            left = mid + 1
            lr_check = 1
            # return binary_search(lst, num)
        else:
            return result

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0

    # 1. 두번째 리스트의 원소들을 차례로 이진탐색 함수에 넣어준다
    for i in B:
        # print(binary_search(A, i))
        # 1-1. 만약 리턴값이 1이라면 카운팅해준다
        if binary_search(A, i):
            cnt += 1
    # 3. 결과값 출력
    print(f'#{tc} {cnt}')