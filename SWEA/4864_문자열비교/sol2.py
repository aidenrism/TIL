import sys
sys.stdin = open('input.txt')

def compare(short, long):
    m = len(short)
    n = len(long)
    st = 0
    while st < n-m+1:
        if long[st:st+m] == short:
            return 1
        else:
            st += 1
    return 0

T = int(input())

for tc in range(1, T+1):
    short = input()
    long  = input()

    print('#{} {}'.format(tc, compare(short, long)))


# a = 'ABC'
# b = 'ABCA'
# print(compare(a, b))
# print(compare('ABC', 'ZZZABCZ'))