import sys
sys.stdin = open('input.txt')

def dfs(num, cnt):
    if num == B:
        global Min
        Min = cnt
        return
    if num*2 <= B:
        dfs(num*2, cnt+1)
    if int(str(num)+'1') <= B:
        dfs(int(str(num)+'1'), cnt+1)


A, B = map(int, input().split())
Min = -1
dfs(A, 1)
print(Min)