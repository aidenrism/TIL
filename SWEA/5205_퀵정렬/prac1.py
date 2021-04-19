import sys
sys.stdin = open('input.txt')


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pibut = numbers[0]
    left = []
    right = []

    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        else:
            right.append(numbers[i])
    return [left, pibut, right]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    print(quick_sort(lst))

