import sys

sys.stdin = open('sample_input.txt')

# 세개씩 묶어서 합을 출력해보는 코드 작성

T = int(input())

for tc in range(1, T + 1):
    # 전체숫자와 구간의 크기
    N, M = map(int, input().split())
    # print(N, M)
    numbers = list(map(int, input().split()))
    # 총합을 담을 리스트
    sum_list = []
    # i값은 총 만드는 묶음 수  6번 반복한다
    for i in range(N - M + 1):
        # 총합의 초기화
        total = 0
        # j 값은 한 묶음의 수 5개씩 더하는 것을
        for j in range(i, M + i):
            total += numbers[j]
        sum_list.append(total)
    # print(sum_list)

    highest = sum_list[0]
    lowest = sum_list[0]

    for idx in sum_list:
        if idx > highest:
            highest = idx
    for idx in sum_list:
        if idx < lowest:
            lowest = idx
    print('#{} {}'.format(tc, highest - lowest))
