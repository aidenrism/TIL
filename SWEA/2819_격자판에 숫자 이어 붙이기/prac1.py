import sys
sys.stdin = open('input.txt')


def make_seven(n, c, r):

        global unique
        global temp
        global emp
        if len(n) == 7:
            unique.add(n)
            # unique.add(emp)
            return
        # else:
            # emp += grid[i][j]
        for dir in range(4):
            n_col, n_row = c + dc[dir], r + dr[dir]
            if 0 <= n_col < 4 and 0 <= n_row < 4:
                make_seven(n+grid[n_col][n_row], n_col, n_row)
            # make_seven(n + grid[i][j], i +1 , j)
            # make_seven(n + grid[i][j], i - 1, j)
            # make_seven(n + grid[i][j], i, j -1 )
            # make_seven(n + grid[i][j], i, j +1 )




T = int(input())
grid = [list(input().split()) for _ in range(4)]
print(grid)
emp = ''
unique = set()
temp = []
dc = (0, 0, -1, 1)
dr = (-1, 1, 0, 0)
for c in range(4):
    for r in range(4):
        make_seven(grid[c][r], c, r)
print(emp)
print(temp)
print(len(temp)) #  2275
cnt = 0
for i in temp:
    ch = ''.join(i)
    unique.add(ch)
    cnt += 1
print(unique)
print(cnt)
print(len(unique))

# print(len(set(temp)))