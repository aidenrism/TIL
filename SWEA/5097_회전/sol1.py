import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # for _ in range(M):
    #     num = numbers.pop(0)
    #     numbers.append(num)
    # print('#{} {}'.format(tc,numbers[0]))

    for _ in range(M):
        numbers.append(numbers.pop(0))
    print('#{} {}'.format(tc, numbers.pop(0)))

    # M = M % N
    # print(numbers[M])

# 리스트 큐
# 원형 큐
# 선형 큐
