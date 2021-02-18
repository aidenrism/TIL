import sys
sys.stdin = open('input.txt')

T = int(input())
students = []
for i in range(T):
    w, h= map(int, input().split())
    # print(*body)
    students.append((w,h))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
