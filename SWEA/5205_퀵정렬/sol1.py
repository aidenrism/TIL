import sys
sys.stdin = open('input.txt')


# 1. 퀵소트 함수적용
def quick_sort(numbers, s, e):
    # s가 e보다 커질 때 리턴
    if s >= e:
        return
    # 기준값은 중간인덱스
    pivot = (s+e)//2
    left = s
    right = e

    # 피봇보다 큰값과 피봇보다 작은 값을 찾을 때까지 left는 1 더해주고 right는 1 빼줌
    while left < right:
        while numbers[left] < numbers[pivot] and left < right:
            left += 1
        while numbers[right] >= numbers[pivot] and left < right:
            right -= 1

        if left < right:
            # 왼쪽원소들이 다 작을 때
            if left == pivot:
                # right가 피봇
                pivot = right
            # 큰 left와 작았던 right를 서로 교환
            numbers[left], numbers[right] = numbers[right], numbers[left]
    # 피봇과 right의 스왑
    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]

    # 새로운 피봇을 기준으로 좌우 퀵소트
    quick_sort(numbers, s, right-1)
    quick_sort(numbers, right+1, e)



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    # 1. 퀵소트 함수적용
    quick_sort(lst, 0, n-1)

    # print(lst)
    # 2. 결과값 출력(중간값)
    print(f'#{tc} {lst[n//2]}')

