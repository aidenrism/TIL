import sys
sys.stdin = open('input.txt')

# 지금부터 인풋이 나오면 알아서 소비시켜준다

# T = int(input())
# for i in range(T):
#     x = input()
#     print(x, type(x))

T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    # print(x, type(x))
    total = 0
    for number in numbers:
        total += number
    # print(f'#{i} {round(total/len(numbers))}')
    print('#{} {}'.format(i, round(total/len(numbers))))
