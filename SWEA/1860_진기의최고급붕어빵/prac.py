


# n =3
# while n > 1:
#     print(n)
#     # for i in range(len(people)):
#     for i in range(4):
#         # if people[0] > m:
#         print(i)
#         if i == 2:
#             break
#     n -=1
#
# people = q_sort(people)
# fish = people[-1] // m * k
# n = len(N)
#
# while n > 1:
#     for i in range(len(people)):
#
#     n -= 1
# print(300//20*3)


T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    for i in range(N - 1):
        for j in range(i + 1, N):
            if people[i] > people[j]:
                people[i], people[j] = people[j], people[i]
    n = len(people)
    i = 0
    fish = 0
    result = 1
    latest = 0
    while n > 0:
        fish += ((people[i] - latest) // m) * k
        latest = (people[i] // m) * m
        if fish > 0:
            fish -= 1
            n -= 1
            i += 1
        else:
            result = 0

        if n == 0 and fish > 0:
            result = 1

    if result:
        result = 'Possible'
        break
    else:
        result = 'Impossible'
        break
    # print(people[0:10])
    print('#{} {}'.format(tc, result))