import sys

sys.stdin = open('sample_input.txt')

# min max함수를 만들어 큰 수와 작은수의 차이를 구하는 문제
# 인풋은 세종류

T = int(input())


for tc in range(T):

    length = int(input())
    numbers = list(map(int, input().split()))


    # print(numbers)
    highest = numbers[0]
    lowest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
            continue
    for num in numbers:
        if num < lowest:
            lowest = num

    print('#{} {}'.format(tc+1, highest-lowest))
