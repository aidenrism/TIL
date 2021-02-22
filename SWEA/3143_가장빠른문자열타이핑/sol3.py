# long = 'cccccc'
# short = 'ccc'
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    long, short = input().split()
    n = len(long)
    m = len(short)
    # print(long,short)
    cnt = 0
    st = 0

    while st < n-m+1:
        if short == long[st:st+m]:
            st += m
            cnt += 1
        else:
            cnt += 1
            st += 1
            if st == n-m+1:
                cnt += m-1
    if st > n-m+1:
        cnt += n-st
    # print(st)
    print('#{} {}'.format(tc, cnt))

