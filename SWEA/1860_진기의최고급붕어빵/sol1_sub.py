def fishcake(m, k, people):
    # people = q_sort(people)
    n = len(people)
    i = 0
    fish = 0
    result = 1
    latest = 0

    while n > 0:
        fish += ((people[i] - latest)// m) * k
        latest = (people[i]//m) * m
        if fish > 0:
            fish -= 1
            n -= 1
            i += 1
        else:
            result = 0
            break
    #     if n > 0:
    #         continue
        if n == 0 and fish > 0:
            result = 1
            break
    #         break
    #     if fish <= 0:
    #         result = 0
    if result:
        return 'Possible'
    else:
        return 'Impossible'


def q_sort(nums):
    if len(nums) <= 1:
        return nums

    left, right = [], []
    pibut = nums[0]

    # 1부터 시작해야 한다!
    for i in range(1, len(nums)):
        if nums[i] < pibut:
            left.append(nums[i])
        else:
            right.append(nums[i])

    sorted_left = q_sort(left)
    sorted_right = q_sort(right)

    return [*sorted_left, pibut, *sorted_right]


T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int,input().split())
    # print(n)
    people = list(map(int, input().split()))

    # result = ''
    # fish = q_sort(people)[-1] // m * k
    # for i in range(len(people)):
    #     if people[i]
    # if n > fish:
    #     result = 'Impossible'
    # else:
    #     result = 'Possible'

    people = q_sort(people)

    print('#{} {}'.format(tc, fishcake(m,k,people)))
