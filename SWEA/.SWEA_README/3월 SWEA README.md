[TOC]

# 3월 SWEA README

 :smiley:  :slightly_smiling_face:  :sweat:  :face_with_head_bandage:

3월 알고리즘도 화이팅

1일 1 commit :checkered_flag: 



## #1225_암호생성기

:slightly_smiling_face: 

```python
T = int(input())
passwords = list(map(int, input().split()))
for num in range(1,6):
    words = passwords.pop(0)
    passwords.append(words - num)
print(passwords)
```

9550 9556 9550 9553 9558 9551 9551 9551 >> [9551, 9551, 9551, 9549, 9554, 9547, 9549, 9553]

이게 한 사이클이다.

숫자중 하나가 0보다 작아질 때 까지 n번 반복.

0보다 작아지면 멈추고 그 값을 0으로 바꿔줘야 함.

```python
# 변수 생성(임시)
new_words = passwords[0]
# 뺀 값이 0보다 클 때 동안 계속 반복
while new_words > 0:
    for num in range(1,6):
        # Queue stack 선입선출! 앞에 값을 계속 뽑는다. 그리고 뒤로 append
        words = passwords.pop(0)
        new_words = words - num
        if new_words < 0:
            new_words = 0
        passwords.append(new_words)
print(*passwords)
```



@@문제에 0보다 작아지는 경우 종료된다고 했는데 실제로는 0과 작거나 같아지는 구간에서 종료해야지 답이 맞게 나온다..

따라서

```python
for _ in range(10):
    T = int(input())
    passwords = list(map(int, input().split()))

    new_words = passwords[0]
    while new_words >= 0:
        for num in range(1,6):
            words = passwords.pop(0)
            new_words = words - num
             # 0보다 작아지는 경우 프로그램 종료
            if new_words < 0:
                break
            passwords.append(new_words)
        # 0보다 작아지는 경우 프로그램 종료
        if new_words < 0:
            new_words = 0
            passwords.append(new_words)
            break

    # passwords = ''.join(passwords)
    # print('{} {}'.format(T, passwords))
    # print('#{} {}'.format(T, passwords))
    # print(*passwords)
    print('#{}'.format(T) , end = ' ')
    print(*passwords)
```

 이렇게해야 통과한다.

```python
new_words = passwords[0]
while new_words > 0:
    for num in range(1,6):
        words = passwords.pop(0)
        new_words = words - num
        if new_words <= 0:
            new_words = 0
            passwords.append(new_words)
            break
        passwords.append(new_words)

print('#{}'.format(T) , end = ' ')
print(*passwords)
```





5의 나머지 연산을 이용하고 마지막 값만 확인하는 간단한 코드

```python
T = 10
 
for _ in range(1, T+1):
    tc = int(input())
    cipher = list(map(int, input().split()))
 
    itr = 0
    while cipher[-1] > 0:
        cipher.append(cipher.pop(0) - (itr % 5 + 1))
        itr += 1
    cipher[-1] = 0
 
    print('#{} {}'.format(tc, ' '.join(map(str, cipher))))
```

다른 코드 (함수를 만들어 사용)

```python
def password(queue):
    while True:
        for i in range(1, 6):
            tmp = queue.pop(0)
            if tmp - i <= 0:
                queue.append(0)
                return queue
            else:
                queue.append(tmp - i)
 
T = 10
for _ in range(1, T + 1):
    tc = int(input())
    queue = list(map(int, input().split()))
    result = ' '.join(map(str, password(queue)))
 
    print('#{} {}'.format(tc, result))
```



## #5097_회전

 :smiley:  

N개의 숫자로 이루어진 수열

M번 앞에 숫자를 뒤로 이동시키기

(Queue 스택)

pop(0)

append(num)

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        num = numbers.pop(0)
        numbers.append(num)
    print('#{} {}'.format(tc,numbers[0]))
```

역시 정답률이 높다





## #5105_미로의거리

3​):sweat:

저번에 4875에서는 dfs 스택을 이용한 미로였고 이번엔 bfs queue 스택을 이용한 미로이다.



갈 수 있다면 최소거리를 못간다면 0 을 출력하는 문제



1. 출발점의 위치를 알아낸다.
2. 델타이동을 한다
3. 도착시 스택의 깊이를 출력한다(한가지이상이라면 최소가 되는 거리를)



```python
def Issafe(y,x):
    return N > x >= 0 and N > y >= 0
def bfs(maze):
    # 상하좌우
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]

    visited = []
    visited.append((col, row))
    m = 0
    # while True:
    for dir in range(4):
        n_col = col + dc[dir] + m
        n_row = row + dr[dir] + m
        if Issafe(n_col,n_row) and maze[n_col][n_row] == 0 :
            print(n_col, n_row)

```

범위가 벗어나지 않고 갈 수 있는 0으로 이동.



```python
def Issafe(y,x):

    return N > x >= 0 and N > y >= 0
def bfs(maze):
    # 상하좌우
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    current = (col, row)

    visited = []
    visited.append(current)
    to_visits = [current]

    while to_visits:
        current = to_visits.pop(0)
        for dir in range(4):

            n_col = current[0] + dc[dir]
            n_row = current[1] + dr[dir]

            if Issafe(n_col,n_row) and maze[n_col][n_row] == 0 :

                if (n_col, n_row) not in visited:
                    visited.append((n_col, n_row))
                    to_visits.append((n_col, n_row))

            elif Issafe(n_col,n_row) and maze[n_col][n_row] == 3:
                return abs(n_col-col)+abs(n_row-row)-1
    return 0

    print(visited)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                col, row = i, j

    print('#{} {}'.format(tc, bfs(maze)))
```

10개 중 4개 pass



위식은 미로가 꼬였을때가 고려되지 않았다. 최소거리만 나옴..



```python
N =5
emp = [[0] * N for _ in range(N)]
visited = [(4, 3), (3, 3), (4, 2), (2, 3), (4, 1), (1, 3), (3, 1), (0, 3), (2, 1), (1, 1), (0, 1)]

for i in range(1,len(visited)):

    emp[visited[i][0]][visited[i][1]] = 1
emp[visited[0][0]][visited[0][1]] = 2
emp[visited[-1][0]][visited[-1][-1]] = 3

for i in emp:
    print(*i)

cnt = 0
for i in range(5):
    for j in range(5):
        if emp[i][j] == 1:
            cnt += 1
print(cnt)
print(len(visited))
```

리스트 원소들을 빈 공간에 체크해주기.

0 3 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 1 2 0





```python
def Issafe(y,x):

    return N > x >= 0 and N > y >= 0

def bfs(maze):
    # 상하좌우
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    # 현재 위치(출발점)
    current = (col, row)
    # 방문체크
    visited = [current]
    # 스택
    to_visits = [current]
    # 거리계산
    distance = [[0]* N for _ in range(N)]
	
    # 스택값이 있는동안 반복
    while to_visits:
        # dfs가 아니라 bfs 넒이중심탐색
        current = to_visits.pop(0)
        # 상하좌우 이동
        for dir in range(4):
            n_col = current[0] + dc[dir]
            n_row = current[1] + dr[dir]

            if Issafe(n_col,n_row) and maze[n_col][n_row] == 0 :
				# 방문하지 않았다면 방문에 체크하고 스택에 값 추가 그리고 범위계산값도 추가
                if (n_col, n_row) not in visited:
                    visited.append((n_col, n_row))
                    to_visits.append((n_col, n_row))
                    distance[n_col][n_row] = distance[current[0]][current[1]] + 1
			# 전 단계값을 산출 
            elif Issafe(n_col,n_row) and maze[n_col][n_row] == 3:
                return distance[current[0]][current[1]]

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                col, row = i, j

    print('#{} {}'.format(tc, bfs(maze)))
```

solving talk에서 0으로 만들어진 2차원 리스트를 만들라는 말을 보고 어떻게 계산해야 할 지 몰랐는데 답을 구했다.

현재값 current 를 기준으로 상하좌우로 이동할 때 distance 이차원 리스트에서는 +1 씩 해주는 것이다.

그렇게 된다면 과녁과 같이 출발점에서 멀어질수록 +1 씩 되어 마지막 값 전까지 계산하면 이동한 거리가 된다.



```python
def IsSafe(y,x):
    return 0 <= y < N and 0<= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def BFS(start_y, start_x):
    global D_result
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            NewY = start_y + dy[dir]
            NewX = start_x + dx[dir]
            if IsSafe(NewY, NewX) and (NewY, NewX) not in visited:
                Q.append((NewY, NewX))
                visited.append((NewY, NewX))
                Distance[NewY][NewX] = Distance[start_y][start_x] +1
                if Maze[NewY][NewX] == 3:
                    D_result = Distance[NewY][NewX] -1
                    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    D_result = 0
    Q = []
    Distance = [[0]*N for _ in range(N)]
    BFS(start_y, start_x)
    print(f'#{tc} {D_result}')
```





## #1226_미로1

0. 5):smiley:

미로 첫번째 learn의 문제와 비슷하다.



dfs 사용

```python
import sys
sys.stdin = open('input.txt')

# 범위를 벗어나지 않고 길로 가는지 체크
def Issafe(y,x):
    return 0 < y < 16 and 0 < x < 16 and (maze[y][x] == 0 or maze[y][x] == 3)

def dfs(y,x):
    visited = []
    to_visits = []
    to_visits.append((st_y, st_x))
	#상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while to_visits:
        y, x = to_visits.pop()
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]

            if Issafe(new_y, new_x) and (new_y, new_x) not in visited:
                visited.append((new_y, new_x))
                to_visits.append((new_y, new_x))
			# 도착점과 좌표가 같으면 1을 출력
            if (new_y, new_x) == (end_y, end_x):
                return 1
    # 그렇지 않으면 0을 출력
    return 0


for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    
    # 출발점과 도착점 부여 
    st_y, st_x = 1, 1
    end_y, end_x = 13, 13

    print('#{} {}'.format(T, dfs(st_y,st_x)))
```



bfs를 사용한 방법

```python
def solution():
    # delta 우하좌상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = [start]
    visited = [[0]*16 for _ in range(16)]
 
    while True:
        for idx in range(4):
            next_x = queue[0][0] + dx[idx]
            next_y = queue[0][1] + dy[idx]
 
            if 0 <= next_x < 16 and 0 <= next_y < 16:
                if matrix[next_x][next_y] == 3:
                    return 1
                elif matrix[next_x][next_y] == 0:
                    if visited[next_x][next_y] == 0:
                        queue.append([next_x, next_y])
 
        visited[queue[0][0]][queue[0][1]] = 1
        if len(queue) >= 2:
            queue.pop(0)
        else:
            return 0
 
 
for _ in range(1, 11):
    case = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                start = [i, j]
 
    print('#{} {}'.format(case, solution()))
```



다른방법의 상하좌우

```python
# 출발점 찾기
def start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return [(i, j)]
 
 # 상하좌우
def escape(road):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    path = []
 
    while road:
        current = road.pop()
        path.append(current)
 		# 현재값의 상하좌우 이동
        for step in direction:
            next = (current[0] + step[0], current[1] + step[1])
            if next not in path and maze[next[0]][next[1]] == 0:
                road.append(next)
            elif next not in path and maze[next[0]][next[1]] == 3:
                return 1
    return 0
 
 
T = 10
for _ in range(1, T + 1):
    tc = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    road = start()
 
    print('#{} {}'.format(tc, escape(road)))
```





## #5099_피자굽기



N개의 피자가 들어가는 화로에 M개의 피자를 굽는다.

치즈의 양 c는 M개의 숫자 리스트로 되어있다.

N개의 피자가 오븐에서 돌고 한바퀴 돌면 c가 //2 만큼 줄어든다.

치즈가 0이 되면 그 피자를 빼고 뒤에 피자를 집어넣는다.



762 >>(한바퀴) 331 >> 110 >> 011 >> 511 >> 005 >> 305 >> 102 >> 110 

```python
N, M = 3, 5
pizzas = [7, 2, 6, 5, 3]

oven = []
cnt = 0
for _ in range(N):
    oven.append(pizzas.pop(0))
cnt += N
# print(oven)
# print(pizzas)

while pizzas:
    for i in range(N):
        print(oven)
        oven[i] = oven[i]//2

        if oven[i] == 0:
            if pizzas:
                oven[i] = pizzas.pop(0)
                cnt = oven[i]
                print(cnt)
    print(oven, 'end')
for i in range(N):
    print(oven, 'new')
    oven[i] = oven[i] //2
print(oven, 'new_end')
```

[7, 2, 6]
[3, 2, 6]
[3, 1, 6]
[3, 1, 3] end
[3, 1, 3]
[1, 1, 3]
[1, 5, 3]
[1, 5, 1] end
[1, 5, 1]
[3, 5, 1]
[3, 2, 1]
[3, 2, 0] end
[3, 2, 0] new
[1, 2, 0] new
[1, 1, 0] new
[1, 1, 0] new_end



idx값을 뽑기 어려움.



피자 넣는다 > 돌린다 (오븐에 세개있을때) > 치즈 0 이면 뺀다, 새로 넣는다 > 돌린다(오븐에 세개있을때) > 치즈 0이면 뺀다, 새로 넣는다 > 마지막 남은 피자 1개면 그피자의 인덱스를 구한다.



2)

안좋고 긴 코드를 계속 수정해서 고치려고 하니까 오래걸렸다..

새로짜는게 빨랐을 수도.. 

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    pizza_idx = list(range(1, M + 1))
    # 오븐에 바로 들어가는 피자들
    oven = pizzas[:N]
    oven_idx = pizza_idx[:N]
    # 오븐에 바로 들어가지 못하는 피자들
    table = pizzas[N:]
    table_idx = pizza_idx[N:]

    while len(oven) > 1:
		# 오븐에 피자가 부족하면 테이블에서 채운다
        if len(oven) < N:
            if len(table) > 0:
                oven.append(table.pop(0))
                oven_idx.append(table_idx.pop(0))
            else:
                # 더이상 채울 값이 없으면 여기서 밑에서 하던 연산을 다시 함
                if len(table) == 0:
                    for _ in range(len(oven)):
                        if len(oven) == 1:
                            last_pizza = oven_idx[0]
                        oven[0] //= 2
                        if oven[0] == 0:
                            oven.pop(0)
                            oven_idx.pop(0)
                        # 앞에 2로 나눈 몫을 빼서 뒤로 붙임
                        else:
                            oven.append(oven.pop(0))
                            oven_idx.append(oven_idx.pop(0))
                    # 오븐에 마지막 하나가 남았으면 그때의 인덱스 값 출력후 멈춤
                    if len(oven) == 1:
                        last_pizza = oven_idx[0]
                        break
		# 오븐에 피자들이 채워져있으면 녹이고 뒤로보내고 queue스택 방식을 사용
        elif len(oven) == N:
            for _ in range(N):
                oven[0] //= 2
                if oven[0] == 0:
                    oven.pop(0)
                    oven_idx.pop(0)
                    break
                else:
                    oven.append(oven.pop(0))
                    oven_idx.append(oven_idx.pop(0))

    print('#{} {}'.format(tc, last_pizza))
```



```python
for tc in range(1, TC+1):
    N,M = map(int, input().split())
    Data = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append([Data[i], i])
    # print(Q)

    i = 0
    while len(Q)!=1:
        Q[0][0] //= 2

        if Q[0][0] == 0:
            if N+ i < M:
                Q.pop(0)
                Q.append([Data[N+i], N+i])
                i+=1
            elif N+i >= M:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))

    print(f'#{tc} {Q[0][1]+1}')
```

간결한 코드



```python
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # N: 동시에 구울 수 있는 피자의 수
                                     # M: 피자의 수
    Ci = list(map(int, input().split())) # 각 피자에서 치즈의 양

    Oven = Ci[:N] # 초기 화덕에 넣은 피자
    # print(Ci)
    # print(Oven)
    Oven_idx = list(range(1, N+1)) # 초기 화덕에 넣은 피자의 인덱스
    # print(Oven_idx)
    mod = Ci[N:] # 완료되는대로 넣을 피자
    mod_idx = list(range(N+1, M+1)) # 완료되는대로 넣을 피자의 인덱스

    while len(Oven) > 1: # 화덕 안에 피자 수가 1개가 남을 때까지 반복
        circle = Oven.pop(0)//2 # 오픈의 첫번째 피자를 꺼냈을 때 남은 치즈의 양
        circle_idx = Oven_idx.pop(0) # 위 피자에 해당하는 인덱스
        if circle == 0: # 남은 치즈의 양이 0이라면
            if len(mod) > 0: # 이 때 화덕에 넣을 수 있는 피자의 양이 0보다 크다면
                Oven.append(mod.pop(0)) # 하나를 빼서 화덕에 넣고
                Oven_idx.append(mod_idx.pop(0)) # 해당 익덱스도 넣는다.
            else: # 그렇지 않다면, 즉 남은 피자의 양이 없다면 뺀걸로 끝났으니 continue
                continue
        else: # 남은 치즈의 양이 0이 아니라면, 다시 넣자.
            Oven.append(circle)  #  다시 화덕에 넣자
            Oven_idx.append(circle_idx) # 인덱스도 다시 넣자

    print('#{} {}'.format(t, *Oven_idx))
```

서클이라는 매개변수를 이용한 코드



## #1974_스도쿠검증





```python
def Isreal(sudoku):
    cnt1 = 0
    cnt2 = 0
    result = 0
    for i in range(9):
        cnt1 = 0
        cnt2 = 0
		
        for j in range(9):
            # 가로계산, 세로계산
            cnt1 += sudoku[i][j]
            cnt2 += sudoku[j][i]
            cnt3 = 0
            
            # 정사각형 9개 계산
            if (i % 3 == 0 and j % 3 == 0):
                for k in range(3):
                    for l in range(3):
                        cnt3 += sudoku[i + k][j + l]
                if cnt3 != 45:
                    result += 1
        if (cnt1 != 45 and cnt2 != 45):
            # if (cnt1 and cnt2) != 45:
            # if cnt1 != 45 and cnt2 != 45:
            result += 1
    if result == 0:
        return 1
    else:
        return 0

    # print(cnt1)
    # print(cnt2)
    # print(cnt3)

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, Isreal(sudoku)))
```

6개 맞음..



​        if (cnt1 != 45 and cnt2 != 45):

or 로 해주지 않아서 30분동안 찾고있었음..

false and true 는 false이다 

true and false 도 false다

그래서 45가 아닌데도 다른 cnt 값이 45이면 반영이 안되었음..

다음부터 주의하자ㅎㅎ





## #1258_ 행렬찾기

2.5) :sweat:

```python
N = int(input())
matrix = [list(map(int, input().split()))for _ in range(N)]
print(matrix)

# 각 행의 창고 행 길이를 저장
cr_list = [[] for _ in range(N)]

for c in range(N):
    # 각 행의 0이 아닌 숫자의 인덱스를 저장
    c_pot = []
    for r in range(N):
        if matrix[c][r] != 0:
            # 창고에 인덱스들을 저장
            c_pot.append(r)
        # 저장하다가 0이 나오면 마지막 인덱스 값+1 저장 (창고의 행길이)
        elif matrix[c][r] == 0:
            while c_pot:
                print(c_pot)
                cr_list[c].append((c_pot.pop())+1)
                c_pot = []
    # 0 이 아닌 숫자가 있는 인덱스들이 있다면
    if c_pot:
        row = c_pot[-1] - c_pot[0] + 1
        cr_list[c].append(row)
print(cr_list)
```



행을 순회하며 0이 아닌값들을  빈 리스트에 넣어주고 0이 나오면 그 리스트의 길이를 cr_list에 append한다 append 이후 c_pot 은 초기화한다.



그리고 0이 나오지 않고 끝나는 경우는 c_pot에 저장된 0이 아닌값들에서 마지막 인덱스 - 첫 인덱스로 행의 길이를 cr_list에 추가한다.



[[4], [4], [4], [5], [3, 5], [3, 5], [5], [], []]

1행에 4짜리 1개 2행에 4짜리 1개 3행에 4짜리 한개.. 이렇게 출력된다.



```python
cnt_list = [[] for _ in range(N)]
for idx in range(N):
    for jdx in range(len(cr_list[idx])):
        row = cr_list[idx][jdx]
        cnt_list[row].append(row)

print(cnt_list)

# 작은것부터 행렬 추출
for i in range(N):
    if cnt_list[i]:
        print(i,len(cnt_list[i]))
```

[[], [], [], [3, 3], [4, 4, 4], [5, 5, 5, 5], [], [], []]
3 2
4 3
5 4

 더하기를 하지못하여 그냥 행의 길이를 행의 위치에 덧붙였다.  그리고 길이를 열의 값으로 계산해주었다.

```tex
#1 1 2 4 1 
#2 3 4 4 2 6 5 7 1 
#3 1 8 3 2 8 5 12 1 15 9 17 3 
#4 10 9 11 10 15 4 20 8 21 2 22 5 24 1 25 6 28 11 29 12 
#5 7 17 10 11 17 15 20 10 24 1 29 6 32 7 33 2 
#6 4 7 6 18 10 1 11 12 12 15 16 6 18 16 24 11 32 13 35 4 
#7 3 6 6 8 10 14 13 1 15 11 19 10 22 19 25 12 33 3 35 4 41 13 51 15 54 7 
#8 3 25 4 3 8 12 12 15 18 11 22 1 26 2 34 8 35 22 36 9 38 4 40 13 42 10 67 18 69 17 
#9 4 14 6 9 7 3 8 11 9 16 10 4 23 20 27 15 35 27 40 7 41 10 42 17 46 8 58 21 64 18 65 6 71 23 88 26 
#10 1 2 6 5 12 30 14 12 21 10 22 15 25 11 33 14 36 21 39 16 41 4 43 6 58 28 61 13 63 25 75 9 87 29 88 8 98 22 99 20 
```

크기는 정렬되지 않음.





##### 문제점

```python
#while c_pot:
#   print(c_pot)
#    cr_list[c].append((c_pot.pop())+1)
#    c_pot = []
while c_pot:
    # print(c_pot)
    temp = c_pot[-1] - c_pot[0] + 1
    cr_list[c].append(temp)
    c_pot = []
```

인덱스길이가 아니라 마지막인덱스+1로 잘못출력되었음



#### 완성코드

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split()))for _ in range(N)]

    # 각 행의 창고 행 길이를 저장
    cr_list = [[] for _ in range(N)]

    for c in range(N):
        # 각 행의 0이 아닌 숫자의 인덱스를 저장
        c_pot = []
        for r in range(N):
            if matrix[c][r] != 0:
                # 창고에 인덱스들을 저장
                c_pot.append(r)
            # 저장하다가 0이 나오면 마지막 인덱스 값+1 저장 (창고의 행길이) --> 오답
            # 임시변수temp로 길이를 계산해서 저장해줌 
            elif matrix[c][r] == 0:
                while c_pot:
                    # print(c_pot)
                    temp = c_pot[-1] - c_pot[0] + 1
                    cr_list[c].append(temp)
                    c_pot = []
        # 0 이 아닌 숫자가 있는 인덱스들이 있다면
        if c_pot:
            row = c_pot[-1] - c_pot[0] + 1
            cr_list[c].append(row)

    cnt_list = [[] for _ in range(N)]
    for idx in range(N):
        for jdx in range(len(cr_list[idx])):
            row = cr_list[idx][jdx]
            cnt_list[row].append(row)

    # 작은것부터 행렬 추출
    cnt = 0
    result = [[] for _ in range(N)]
    for i in range(N):
        if cnt_list[i]:
            cnt += 1
            result[i] += [len(cnt_list[i]), i]
    result1 = [[]for _ in range(N)]
	
    # 행렬의 곱과 행 열을 차례로 빈 리스트에 더해줌 
    for i in range(N):
        if result[i]:
            area = result[i][0] * result[i][1]
            result1[result[i][0]-1].append(area)
            result1[result[i][0] - 1].append(result[i][0])
            result1[result[i][0] - 1].append(result[i][1])
	# 크기를 기준으로 오름차순 정렬 
    result1 = sorted(result1)
    print()
    # print(result1)

    print('#{} {}'.format(tc, cnt), end=' ')
    for i in range(len(result1)):
        if result1[i]:
            print(*result1[i][1:], end=' ')
```



짧게 짠 코드들

```python
T = int(input())
 
for tc in range(1, T+1):
    n = int(input()) # matrix 수
    matrix = [
        list(map(int, input().split())) for _ in range(n)
    ]
 
    ans = []
 
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                r, c = i, j
                while r < n and matrix[r][j] != 0:
                    r += 1
                while c < n and matrix[i][c] != 0:
                    c += 1
                # ans 는 행렬의 행과 열을 한 쌍으로 정리해둔 리스트
                ans.append([r-i, c-j])
 
 
                # 초기화 작업 (그래야 다음 번에 돌 때 그 행렬은 지나감)
                for a in range(i,r):
                    for b in range(j,c):
                        matrix[a][b] = 0
 
     # 행렬 크기 곱한 순으로    
    ans.sort(key=lambda x: (x[0] * x[1], x[0]))
    # tc 넘버와 행렬의 갯수 프린트
    print('#{} {}'.format(tc, len(ans)), end=" ")
 
    # 행렬 리스트 안에 있는 답들을 하나씩 꺼내
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end = " ")
    print()
```



함수만들어 사용

```python
def find_chemicals():
    def is_chemical(r, c):
        return 0 <= r < n and 0 <= c < n and bunker[r][c]
 
    def chemical_box(i, j):
        r, c = i, j
        # 마지막 행 확인
        while is_chemical(r, c):
            r += 1
        row_len = r - i
 
        while is_chemical(r-1, c):
            c += 1
        col_len = c - j
 
        for row in range(i, r):
            for col in range(j, c):
                bunker[row][col] = 'C'
 
        return [row_len, col_len]
 
    chemicals = []
    for i in range(n):
        for j in range(n):
            if bunker[i][j] and bunker[i][j] != 'C':
                chemicals += [chemical_box(i, j)]
 
    return sorted(chemicals, key=lambda x: (x[0] * x[1], x[0]))
 
 
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    bunker = [list(map(int, input().split())) for _ in range(n)]
    result = find_chemicals()
    print('#{} {}'.format(tc, len(result)), end=' ')
    for box in result:
        for num in box:
            print(num, end=' ')
    print()
```



퀵소트 사용 

```python
def quicksort(targets):
    if len(targets) < 2:
        return targets
    pivot = targets[0]
    size = pivot[0] * pivot[1]
    left, right = [], []
    for i in range(1, len(targets)):
        x, y = targets[i]
        if x * y > size or x * y == size and x > pivot[0]:
            right.append(targets[i])
        else:
            left.append(targets[i])
    return [*quicksort(left), pivot, *quicksort(right)]
 
 
def solution():
    submats = []
    # 각 행 내에서 이동하며 시작점 확인
    for i in range(N+1):
        start_j = end_j = -1
        for j in range(N+1):
            # 초기상태
            if start_j == -1:
                # 시작점을 찾으면 기록
                if matrix[i][j]:
                    start_j = j
            # 0이 아니라면 0이 나올 때까지 확인
            else:
                # 도착점을 찾으면 기록
                if not matrix[i][j]:
                    end_j = j
                    # 하단에 0이 나올 때까지 확인
                    for inner_i in range(i, N+1):
                        # 0이 나오면 크기를 submats에 저장 후 초기화
                        if not matrix[inner_i][j-1]:
                            submats.append([inner_i-i, end_j-start_j])
                            start_j = end_j = -1
                            break
                        # 0이 아니라면 지나온 범위 내의 가로를 모두 0으로 변경
                        else:
                            for inner_j in range(start_j, end_j):
                                matrix[inner_i][inner_j] = 0
 
    # submats 정렬: 크기, i 순
    return str(len(submats)) + ' ' + ' '.join(' '.join(i) for i in [list(map(str, i)) for i in quicksort(submats)])
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[*map(int, input().split()), 0] for _ in range(N)]
    matrix.append([0 for _ in range(N+1)])
    print('#{} {}'.format(tc, solution()))
```





좌표와  넓이를 구하고 sorting을 진행한 후 에 초기화해준 코드 (카운트정렬)

```python
# 사각형의 크기를 찾아주는 함수
def search_size(r,c):
    r_cnt = 0
    c_cnt = 0

    # 행의 길이를 찾는
    for i in range(r, N):
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break
    # 열의 길이를 찾는
    for i in range(c, N):
        if arr[r][i] != 0:
            c_cnt += 1
        else:
            break

    ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
    init(r, c, r_cnt, c_cnt)

# 화학물질을 빈용기로 변환
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r_cnt):
        for j in range(c, c_cnt):
            arr[i][j] = 0

def counting_sort(idx): # 첫번째 기준으로 정렬할거냐 두번째 변수를 기준으로 정렬할거냐
    cnt = [0] * 10001
    sort_ans = [0] * len(ans)

    # 1. 카운팅 하는 과정
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1

    # 2. 누적
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    # 3. 정렬하여 넣는 과정
    for i in range(len(ans)-1, -1, -1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1

    return sort_ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    ans = []

    # 행우선순회 방식으로 순회하면서 사각형의 시작좌표를 구한다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0
                search_size(i,j)

    ans = counting_sort(0) # 행을 기준으로 정렬
    ans = counting_sort(2) # 행렬의 크기로 다시한번 정렬

    print('#{} {}'.format(tc, len(ans)), end= ' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end= ' ')
    print()

################################################################

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                #범위를 앞에 위치
                while c < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1

                ans.append([r-i, c-j])

                # 초기화 하는 과정
                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0

    # 첫번째 곱한값을 기준으로 정렬하고 안되면 다음값을 기준으로 정렬
    ans.sort(key = lambda x : (x[0]*x[1], x[0]))
    print('#{} {}'.format(tc, len(ans)), end= ' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end= ' ')
    print()
```



## #1966_숫자정렬

0.5)  :slightly_smiling_face:

bubble  소팅과 quick 소팅을 사용해보았다.

퀵소팅이 완벽히 숙지가 되지않아서 몇군데 헷갈렸다.





```python
def bubblesort(numbers):

    big = numbers[0]
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] < numbers[i-1]:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
    return numbers


def q_sort(numbers):
    # global numbers

    ## len(numbers) == 1 로 하면 비어있을때 (0개있을때) 인덱스 에러가 난다.
    if len(numbers) <= 1:
        return numbers
    pibut = numbers[0]
    left = []
    right = []
    # sorted_left =
    # sorted_right =

    # 1부터 시작해야지 피벗의 반복을 막는다
    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        elif numbers[i] >= pibut:
            right.append(numbers[i])

    sorted_left = q_sort(left)

    sorted_right = q_sort(right)

    # *안해주면 [[0], 1, [[], 4, [[], 7, [8]]]] 다중리스트로 출력된다
    return [*sorted_left, pibut, *sorted_right]


numbers = [1, 4, 7, 8, 0]
print(bubblesort(numbers))

print(q_sort(numbers))
```

sorted_left와 sorted_right 에서 left리스트와 right 리스트를 퀵 소팅해줄때 이미 길이가 1이어서 리턴된 값들은 소팅할 값이 없을 수 있으므로 반드시 ==1 일 떄 반환이 아니라

```python
if len(numbers) <= 1:
    return numbers
```
이하로 선언해주어야 한다.

그리고 left와 right를 나눌때는 for문을 pibut 자기 자신을 제외한 1부터 끝까지 돌려야 한다.



[] 를 제거하는 출력방식은 밑에 방법도 있다.

```python
number = q_sort(numbers)
# print('#{}'.format(tc), end=' ')
# print(*result)

result = ' '.join([str(num) for num in number])
print('#{} {}'.format(tc, result))

list_num = ' '.join(map(str, list_num))
print('#{} {}'.format(tc+1, list_num))
```



## #2805_농작물 수확하기

2)



```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # crops = [list(map(int, input().split())) for _ in range(N)]
    crops = [list(map(int, input())) for _ in range(N)]

    # print(crops)
    # print(crops[0][0])

    mid = N // 2
    k = 0
    revenue = []
    
    # for i in range(N):
    #     for j in range(N):
    #         if i == mid:
    #             revenue.append(crops[i][j])
    #         elif i == 0 or i == N-1:
    #             if j == mid:
    #                 revenue.append(crops[i][mid])
    #         elif i == 1 or i == N-1-1:
    #             if mid-1 <= j <= mid+1:
    #                revenue.append(crops[i][j])
    #     # revenue.append(crops[i][mid])
    # print(revenue)
	
    # 위에서 숫자대신 변수를 활용하면 길이가 달라도 조건을 일일히 부여하지 않아도 되겠다고 생각
    # 임의변수 k를 활용하여 완전탐색을 해줌
    # 중간지점까지 반복해주면서 양쪽 끝에서부터 중앙으로 갈 수록 가운데에서 범위를 넓혀줌
    while k <= mid:
        for i in range(N):
            for j in range(N):
                if i == k or i == N - 1 - k:
                    if mid - k <= j <= mid + k:
                        revenue.append(crops[i][j])
        k += 1
    print('#{} {}'.format(tc, sum(revenue)))
```



행이 중앙에 가까워질수록 j값을 점점 늘려서 빈리스트에 추가하였다. 