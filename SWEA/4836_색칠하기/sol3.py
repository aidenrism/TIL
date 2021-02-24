import sys
sys.stdin = open('input.txt')

test_case = int(input())

for i in range(test_case):
    givens = [[0] * 10 for i in range(10)]
    cnt = 0
    colors = int(input())
    for j in range(colors):
        r1, c1, r2, c2, color_num = map(int, input().split())

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                givens[r][c] += color_num

        for c_lengths in range(10):
            for r_lengths in range(10):
                if givens[c_lengths][r_lengths] == 3:
                    cnt += 1
    print('#{0} {1}'.format(i + 1, cnt))