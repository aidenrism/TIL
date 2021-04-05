import sys
sys.stdin = open('input.txt')


for tc in range(1, 2):
    n = int(input())

    node = [[0]] + [list(map(str, input().split())) for _ in range(n)]
    print(node)