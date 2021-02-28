import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    short = input()
    long  = input()

    n = len(long)
    m = len(short)

    st = 0
    cnt = 0
    while st < n - m + 1:
        if long[st:st + m] == short:
            st += m
            cnt += 1
        elif long[st:st + m] != short:
            st += 1
    if cnt > 0:
        compare = 1
    else:
        compare = 0

    print('#{} {}'.format(tc, compare))






# short = 'ABC'
# long = 'ZZZABZZZ'
