import sys

sys.stdin = open('input.txt')

# test case 개수
T = int(input())
# tc동안 순회

for tc in range(1, T + 1):

    # 리스트의 길이
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # total = 0
    cnt_list = []
    # 길이 비교하여 길이가 작은 리스트가 순회하게 함
    if N > M:

        for idx in range(N - M + 1):
            total = 0
            for i in range(M):
                total += A[i + idx] * B[i]
            # 더한 값들을 빈 리스트에 담는다
            cnt_list.append(total)

        # print(cnt_list)
    elif N == M:

        for idx in range(N - M + 1):
            total = 0
            for i in range(N):
                total += A[i] * B[i]
            # 더한 값들을 빈 리스트에 담는다
            cnt_list.append(total)

    # 만약 A가 더 작으면 A가 순회
    else:
        for idx in range(M - N + 1):
            total = 0
            for i in range(N):
                total += B[i + idx] * A[i]

            cnt_list.append(total)

        # print(cnt_list)

    # 값을 비교해서 큰값 구하기
    highest = cnt_list[0]
    for num in cnt_list:
        if num > highest:
            highest = num

    print('#{} {}'.format(tc, highest))
