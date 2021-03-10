import sys
sys.stdin = open('input.txt')

N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

# pipe
house[0][0], house[0][1] = 'p1','p2'
print(house)

dc = [0, 0]
dr = [1, 1]
# 우로 이동
# m = 1
# for i in range(N-1,-1,-1):
#     for j in range(N-1,-1,-1):
#         if house[i][j] == 'p':
#             if house[i][j+m] == 0:
#                 house[i][j] = 0
#                 house[i][j+m] = 'p'
# print(house)

# 우하로 이동
m = 1
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if house[i][j] == 'p2':
            if house[i][j+m] == 0 and house[i+m][j+m] == 0 and house[i+m][j] == 0:
                house[i][j] = 0
                house[i+m][j+m] = 'p2'
        if house[i][j] == 'p1':
            if house[i+m][j+2] == 'p2':
                house[i][j] = 0
                house[i][j + m] = 'p1'

print(house)
n = N
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
print(dp)
dp[0][1][0] = 1
print(dp)