import sys
sys.stdin = open('input.txt')


def bubblesort(numbers):

    big = numbers[0]
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] < numbers[i-1]:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
    return numbers


def q_sort(numbers):
    # global numbers

    ## len(numbers) == 1 로 하면 비어있을때 (0개있을때) 인덱스 에러가 난다.
    if len(numbers) <= 1:
        return numbers
    pibut = numbers[0]
    left = []
    right = []
    # sorted_left =
    # sorted_right =

    # 1부터 시작해야지 피벗의 반복을 막는다
    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        elif numbers[i] >= pibut:
            right.append(numbers[i])

    sorted_left = q_sort(left)

    sorted_right = q_sort(right)

    # *안해주면 [[0], 1, [[], 4, [[], 7, [8]]]] 다중리스트로 출력된다
    return [*sorted_left, pibut, *sorted_right]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(bubblesort(numbers))
    number = q_sort(numbers)
    # print('#{}'.format(tc), end=' ')
    # print(*result)

    result = ' '.join([str(num) for num in number])
    print('#{} {}'.format(tc, result))
