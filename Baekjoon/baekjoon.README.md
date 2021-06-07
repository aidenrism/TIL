[toc]

# BOJ 문제풀이 

 :smiley:  :slightly_smiling_face:  :sweat:  :face_with_head_bandage:

 ## #1449_수리공항승 



첫번째 순회는 0 1 2 3

두번째는 그것보다 1더한값으로 시작해야함

테이핑 범위안에 있는 숫자들중 가장 큰숫자를 찾아주고 

그거보다 작은 값들은 continue로 넘긴다

그리고 다시 그 기준값보다 큰값이 나타나면 테이핑을 한다.

```python
# 0번부터 테이프 길이까지의 범위안에 속한 곳인지 아닌지 판단하는 기준점 
stand_num = 0

# 누수 파이프의 하나전꺼까지 순회 
for idx in range(N-1):
    if stand_num > idx:
        continue
    else:
        stand_num = 0 
        emp = [] 
        for j in range(idx+1, N):
            if location[j] - location[idx] <= N+1:
                emp.append(j)
            else:
                continue
        
        # select_list.append(my_max(emp))
        stand_num += my_max(emp)
        count += 1
    # print(emp)
print(count)
```



```python
# 누수 파이프의 정렬이 안되어있음을 가정하고 정렬함수를 만들어 정렬을 해줌
def my_sort(x):
    for i in range(len(x)-1):
        if x[i+1] < x[i]:
            x[i], x[i+1] = x[i+1], x[i]
    return x

test11 = [1, 3, 2, 5]
print(my_sort(test11))

```

구글링해서 뭐가 문제일까 살펴보니 정렬을 안해줬을 때 문제가 생긴다는것을 알게 되어서 정렬하는 함수를 버블소팅으로 만들어줌

```python
# 0번부터 테이프 길이까지의 범위안에 속한 곳인지 아닌지 판단하는 기준점 
start = location[0]
end = location[0] + L

# 누수 파이프의 하나전꺼까지 순회 
for idx in range(N):
    if start <= location[idx] < end:
        continue
    else:
        start = location[idx]
        end = location[idx] + L 
        count += 1
            
print(count)
```

테이프 길이를 더한거보다 작으면 넘어가고

크다면 그 값을 다시 스타트 값으로 바꾸고 end를 거기서 테이프 길이만큼 더해주고 카운트를 1늘려주는 식으로 하면 간단하게 구현되는거였다..

구글링 참고..



***

## #4949번_균형잡힌 세상

빈리스트에 괄호들을 넣고 

```python
brackets = ['(', '[', ']', ')']
# brackets = """'(', '[', ']', ')'"""

emp = []

sentence = input()
for word in sentence:
    for bracket in brackets:
        if word == bracket:
            emp.append(word)

print(emp, type(emp))
print(emp[0], type(emp[0]))
print(emp[1], type(emp[1]))
    
```

$ python 4949.py
['(', '[', ']', '(', ')', ')'] <class 'list'>
( <class 'str'>
[ <class 'str'>



```python
for _ in range(len(emp)):
    for idx in range(len(emp)-1):
        # if '[ , ]' or '(, )' = emp[idx], emp[idx+1]:
            print(emp[idx], emp[idx+1])
                print(1)
                if len(emp) == 0:
                    print(2)
                    break
            else:
                continue
```

[ ]
] (
( )
) )
( [
[ ]
] (
( )
) )
( [
[ ]
] (
( )

![image-20210214182323072](C:\Users\a\알고리즘\Baekjoon\baekjoon.README.assets\image-20210214182323072.png)

![image-20210214182355960](C:\Users\a\알고리즘\Baekjoon\baekjoon.README.assets\image-20210214182355960.png)



#### 리스트 원소 없애는 법

![image-20210214183857836](C:\Users\a\알고리즘\Baekjoon\baekjoon.README.assets\image-20210214183857836.png)



$ python list_prac.py
Traceback (most recent call last):
  File "list_prac.py", line 5, in <module>
    kospi_top5.remove(kospi_top5[3], kospi_top5[4])
TypeError: remove() takes exactly one argument (2 given)



리무브는 1개 원소만 지우기 가능

![image-20210214184034760](C:\Users\a\알고리즘\Baekjoon\baekjoon.README.assets\image-20210214184034760.png)

del 은 두개 지울 수 있다!



![image-20210214185510530](C:\Users\a\알고리즘\Baekjoon\baekjoon.README.assets\image-20210214185510530.png)

idx는 늘어나게 설정했지만 emp의 원소들은 줄어들어서 인덱스 범위를 초과하였다

만약에 remove를 성공했다면 돌리는 idx값을 줄여줘야함



![image-20210214192250664](C:\Users\a\알고리즘\Baekjoon\baekjoon.README.assets\image-20210214192250664.png)

갈 수 있나?



```python
while True:
    bracket = input()
    if bracket == ".":
        break
    bracket_stack = []
    answer = True
    
    for j in bracket:
        if j == "(" or j == "[":
            bracket_stack.append(j)
        
        elif j == ")":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                answer = False
                break
                
        elif j == "]":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                answer = False
                break

    if answer and not bracket_stack:
        print("yes")
    else:
        print("no")
      
```

구글링 해보니 애초에 괄호에 해당하는것을 다 뽑아오고 계산하지 않고

여는 괄호 조건일 때는 append하고 닫는 괄호조건일 때 

빈 리스트에 값이 있었는지, 있었다면 같은 유형의 괄호인지를 판단해서 기존 괄호를 리스트에서 제거해주거나 다른 유형일때에 break로 for 문에서 빠져나와서  no를 출력해줄 수 있도록 하였다.



## #2669_직사각형

사각형의 면적들을 구하기 위해서는 각 열의 2행-1행 * 4행-3행을 하면된다

하지만 겹치는 부분을 구하는게 단순하지 않다

0 1 / 0 2 / 0 3 / 1 2 / 1 3/ 2 3 

6개를 비교하고

그냥 부분집합마다 비교를 해야한다

```python
hundred = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    cnt = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if hundred[i][j] == 0:
                hundred[i][j] == 1
                cnt += 1
    print(cnt)
    # print(x1)
    # print(hundred)
```

6
12
12
3

cnt 위로 올리고 print 밖으로 빼주면 33나옴

j i 바꿔줘도 똑같음

==1이 잘못되었다. =1 로 해줘야 중복값이 빠진다.





## #7568_덩치

몸무게와 키가 주어진다

몸무게와 키가 나머지 사람들보다 크면 그 사람은 덩치가 가장 큰 사람이다

하지만 몸무게는 다른 사람보다 크지만 키가 작으면 덩치가 크다고 표현하지 못한다

따라서 키와 몸무게가 다른사람들보다 둘다 작다면 등수가 밀려나고 둘다 높아야만 등수가 올라간다.



인풋개수만큼 등수를 표현한다.



```python
for i in range(5):
    body = map(int, input().split())
    print(*body) # *안써주면 그냥 map 객체로 나옴

```



```python
students = []
for i in range(5):
    w, h= map(int, input().split())
    # print(*body)
    students.append((w,h))

print(students[0])
```

튜플로 묶어주면 두개가 하나로 묶여 append 가능하고 리스트에 집어넣을 수 있음

브루트포스 알고리즘으로

리스트 각 원소의 w와 h를 같이 and와 이중포문으로 다른 원소들과 비교해주어

초기값 = 1 그리고 만약 다른 원소들보다  두값이 동시에 작다면 rank를 +1 해주면 각 원소들의 등수를 첫원소부터 마지막 원소들까지 출력시킬 수 있다.

print에 end값을 ' ' 공백으로 주어야 한다.



```python
students = []
for i in range(5):
    w, h= map(int, input().split())
    # print(*body)
    students.append((w,h))

 # 브루트포스 알고리즘 두가지의 값을 순차적으로 비교
# n명을 n-1번씩 순차적으로 전수 비교
for i in students:
    rank = 1
    for j in students:
        # i순서의 몸무게가 다른것들(n-1개)의 몸무게보다 작고 키도 마찬가지로 작으면 rank를 더해줌
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

```



## #1316_그룹단어체커

aabbcc , kin ccazzz 는 그룹단어

aba, eewwe 는 그룹단어가 아니다.

연속해서 단어가 나타나야한다.



단어는 100보다 작거나 같은 단어의 개수가 들어온다.

주어진 단어들을 돌려서 기존에 있던 값이 나온다면 카운트 시키지 않고 

그룹단어가 나오면 count를 해준다.



그래서 어떻게 기존에 있던 단어가 나올건지 구분할거냐하면 

dict를 이용하여 기존에 없던 값들이면 빈 딕셔너리 키값으로 넣어주고 

만약 있던 값들이면 다시 if else 분기로 나누어 판가름해준다.

만약  word의 i-1인덱스과 다르다면 False를 return 해주고 아니라면 counting을 해주는 함수를 만들었다.

만약 False가 되지 않는다면 True를 return해준다.



```python
def group_word(word):
    n = len(word)
   # group_cnt = 0
    emp = {}
    for i in range(n):
        if word[i] not in emp:
            emp[word[i]] = 1
        else:
            if word[i-1] != word[i]:
                # print('no')
                return False
            else:
                emp[word[i]] += 1
    return True
```

```python
T = int(input())

cnt = 0
for _ in range(T):
    word = input()
    cnt += group_word(word)

print(cnt)
```

그리고 들어오는 단어들에 이 함수를 적용해준다.

3
happya
new
year
2 :ok:정답

 

## #2578_빙고

2.5)​ :sweat: 

```python
bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]
# 2차원 리스트
# print(bingo)
# print(check)

check_lst = []
for i in range(len(check)):
    for j in range(len(check[0])):
        check_lst.append(check[i][j])
# print(check_lst)

cnt = 0
total = 0
for idx in check_lst:
    for i in range(len(bingo)):
        line_cnt = []
        for j in range(len(bingo[0])):
            if bingo[i][j] == idx:
                bingo[i][j] = 1
                cnt += 1
                line_cnt.append(bingo[i][j])
            if sum(line_cnt) == 5:
                total += 1
    if total == 3:
        print(cnt)

```

이렇게 한다면 line_cnt가 줄이 바뀔때마다 1이 5개 있다면 빙고를 세줌



```python
check_lst = []
for i in range(len(check)):
    for j in range(len(check[0])):check_lst.append(check[i][j])
# print(check_lst)

cnt = 0
result = []
line_cnt4 = 0
for idx in check_lst:
    cnt += 1
    # 가로로 빙고 세기
    line_cnt3 = 0

    for i in range(len(bingo)):
        line_cnt1 = 0
        line_cnt2 = 0
        for j in range(len(bingo[0])):
            if bingo[i][j] == idx:
                bingo[i][j] = 1
            line_cnt1 += bingo[i][j]
            line_cnt2 += bingo[j][i]
            if line_cnt1 == 5:
                result.append(1)
            if line_cnt2 == 5:
                result.append(1)
            if i == j:
                line_cnt3 += bingo[i][j]
                if line_cnt3 == 5:
                    result.append(1)
    for ldx in range(len(bingo)):
        for jdx in range(len(bingo)-1,-1,-1):
            if ldx == 0 and jdx == 4:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 1 and jdx ==3:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 2 and jdx == 2:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 3 and jdx == 1:
                line_cnt4 += bingo[ldx][jdx]
                break
            elif ldx == 4 and jdx == 1:
                line_cnt4 += bingo[ldx][jdx]
                break
    if line_cnt4 == 5:
        result.append(1)

    if len(result) == 3:
        print(cnt)
        break

```

개수가 맞게 안나온다.



구글링하다가  빙고를 카운팅하는 함수를 갖다 사용함..

```python
def finder(ptable):
    bingoCount = 0
    for Py in range(5):
        if (ptable[Py][0] == ptable[Py][1] == ptable[Py][2] == ptable[Py][3] == ptable[Py][4] == 1):
            bingoCount += 1

    for Px in range(5):
        if (ptable[0][Px] == ptable[1][Px] == ptable[2][Px] == ptable[3][Px] == ptable[4][Px] == 1):
            bingoCount += 1

    if (ptable[0][0] == ptable[1][1] == ptable[2][2] == ptable[3][3] == ptable[4][4] == 1):
        bingoCount += 1

    if (ptable[0][4] == ptable[1][3] == ptable[2][2] == ptable[3][1] == ptable[4][0] == 1):
        bingoCount += 1

    return bingoCount
```

이 함수를 사용한다면

```python
bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]
# 2차원 리스트
# print(bingo)
# print(check)

# 체크 리스트에 값들을 인덱스 순서대로 더해줌. 나중에  for문을 쉽게 돌리려고
check_lst = []
for i in range(len(check)):
    for j in range(len(check[0])):check_lst.append(check[i][j])
# print(check_lst)

cnt = 0
result = []
# 체크리스트 한번씩 숫자가 나올때마다 카운트 1씩 증가
for idx in check_lst:
    cnt += 1
    # 해당되는 빙고판의 값을 1로 변경해주기
    for i in range(len(bingo)):
        for j in range(len(bingo[0])):
            if bingo[i][j] == idx:
                bingo[i][j] = 1
    # 이전에 가로 세로 양 대각선의 값이 1일때 카운팅을 해주는 함수 사용
    if finder(bingo) >= 3:
        print(cnt)
        break

```

해당되는 값에 1만 넣고  체크리스트에서 idx 돌리는 값이 끝나기전에 함수로 체크해주면 된다.

 

## #2628_종이자르기

```python
row, col = map(int, input().split())
n = int(input())

cut = []
for idx in range(n):
    cut_idx = list(map(int, input().split()))
    # print(*cut_idx)
    cut.append(cut_idx)
print(cut)
```

[[0, 3], [1, 4], [0, 2]]

2차원 리스트 받기

세로의 자르고나서 큰 구간 리스트와 가로의 자르고 나서 큰 구간을 리스트에 각각 넣어준다

[5, 6]
[6]

리스트중 작은 값을 뽑아준다.(퀵정렬 사용)

```python
print(q_sort(y_list)[0])
print(q_sort(x_list)[0])
```

5
6

두값을 곱해준다.

30

-----반례가 많아서 새로 시작

```python
for idx in range(n):
    cut_idx = list(map(int, input().split()))
    # 가로로 자를때 ==> 세로를 봐야함.
    if cut_idx[0] == 0:
        y_list.append(cut_idx[1])
y_list.append(0)
y_list.append(col)
print(q_sort(y_list))
```

[0, 2, 3, 8]

세로값들을 받아주고 i와 i-1의 값을 빼주며 그 값을 비교할 것이다.

```python
y_list = q_sort(y_list)
section = []
for i in range(len(y_list)-1, 0, -1):
    section.append(y_list[i]-y_list[i-1])
print(q_sort(section))
```

[1, 2, 5]

이제 여기서 큰값과 x의 큰값을 곱해주자.

[0, 2, 3, 8]
[0, 4, 10]
[1, 2, 5]
[4, 6]
30



```python
# 퀵정렬
def q_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right = [], []
    pibut = nums[0]
    for idx in range(1, len(nums)):
        if nums[idx] < pibut:
            left.append(nums[idx])
        else:
            right.append(nums[idx])

    sorted_left = q_sort(left)
    sorted_right = q_sort(right)
    return [*sorted_left, pibut, *sorted_right]

## input 시작
row, col = map(int, input().split())

n = int(input())

cut = []
x_list = []
y_list = []

for idx in range(n):
    cut_idx = list(map(int, input().split()))
    # 가로로 자를때 ==> 세로를 봐야함.
    if cut_idx[0] == 0:
        y_list.append(cut_idx[1])
    else:
        x_list.append(cut_idx[1])

y_list.append(0)
y_list.append(col)
x_list.append(0)
x_list.append(row)

# print(q_sort(y_list))
# print(q_sort(x_list))

y_list = q_sort(y_list)
x_list = q_sort(x_list)
section_y = []
section_x = []

for i in range(len(y_list)-1, 0, -1):
    section_y.append(y_list[i]-y_list[i-1])
# print(q_sort(section_y))

for k in range(len(x_list)-1, 0, -1):
    section_x.append(x_list[k]-x_list[k-1])
# print(q_sort(section_x))

x, y = [], []
try:
    y = q_sort(section_y)[-1]
    x = q_sort(section_x)[-1]
except:
    if x:
        pass
    else:
        x = row
    if y:
        pass
    else:
        y =col
print(x*y)
```

코드가 길긴하지만 알아보기엔 쉬울지도..모르겠다.



## #1260_DFS와BFS

2.5)

https://www.acmicpc.net/problem/1260

visited로 체크하려고 했다가 완성하지 못한 코드

```python
def dfs(V):
    
    visited = [False for _ in range]


N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2] += [v1]

#     print(fr, to)
# print(N,M,V)
print(graph)
visited = [False for _ in range(N+1)]
print(dfs(V))
# print(result)
```



dfs  - with stack

```python
def dfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    # 방문한 값들 (길들)
    path = []
	
    # 스택에 쌓인 값들이 있는 동안 반복
    while to_visits:
        # 뒤쪽에서부터 추출 
        current = to_visits.pop()
        # for idx in to_visits:
        if current not in path:
            # current = True
            path.append(current)
            # print(current)
            # 작은 값들부터 확인한다고 문제에서 나왔으므로 정렬후 4321 로 해야 마지막 인덱스인 1으로 뻗어나간다.
            to_visits += sorted(G[current])[::-1]
    return path

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    # 단방향이 아니라 양방향이므로 양쪽에 from to 가 아닌 양쪽으로 append
    G[v2].append(v1)
    G[v1].append(v2)


print(dfs(V))
# print(G)
```



bfs - with stack

```python
def bfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    path = []

    while to_visits:
        # for _ in range(len(to_visits)):
        # 처음 시작점에서부터 인접한 값들부터 방문할 것이므로 첫값에서 append된 앞쪽부터 살펴본다
        # 이 값들에서 나온 값들은 뒤에 append되므로 나중에 방문하지 못하였을시 방문하게된다.
         current = to_visits.pop(0)
        # for idx in to_visits:
         if current not in path:
            # current = True
            path.append(current)
            # print(current)
            # pop을 앞에서 부터 하고 작은값부터 문제에서 방문하기로 하였으므로 오름차순 정렬
            to_visits += sorted(G[current])
    return path

for tc in range(2):
    N, M, V = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        G[v2].append(v1)
        G[v1].append(v2)



    print(bfs(V))
    print(G)
```



합친코드

```python
def dfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    path = []

    # 스택에 쌓인 값들이 있는 동안 반복
    while to_visits:
        # 뒤쪽에서부터 추출 
        current = to_visits.pop()
        # for idx in to_visits:
        if current not in path:
            # current = True
            path.append(current)
            # print(current)
            # 작은 값들부터 확인한다고 문제에서 나왔으므로 정렬후 4321 로 해야 마지막 인덱스인 1으로 뻗어나간다.
            to_visits += sorted(G[current])[::-1]
    return path

def bfs(V):
    # visited = [False for _ in range(N+1)]
    to_visits = [V]
    path = []

    while to_visits:
        # for _ in range(len(to_visits)):
        # 처음 시작점에서부터 인접한 값들부터 방문할 것이므로 첫값에서 append된 앞쪽부터 살펴본다
        # 이 값들에서 나온 값들은 뒤에 append되므로 나중에 방문하지 못하였을시 방문하게된다.
         current = to_visits.pop(0)
        # for idx in to_visits:
         if current not in path:
            # current = True
            path.append(current)
            # print(current)
            # pop을 앞에서 부터 하고 작은값부터 문제에서 방문하기로 하였으므로 오름차순 정렬
            to_visits += sorted(G[current])
    return path

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v2].append(v1)
    G[v1].append(v2)

print(*dfs(V))
print(*bfs(V))
```



새로운 값에 대한 처리가 안된 코드

```python
def dfs(V):
    path = []
    to_visits = [V]
    
    v = to_visits.pop()
    if v not in path:
        path.append(v)
        new_v = sorted(G[v])[0]
        dfs(new_v)
```



dfs - with recursive

```python
def dfs(V):
	# 계속 한개씩 들어감
    to_visits = [V]
    v = to_visits.pop()
    if v not in path:
        path.append(v)
        # new_v = 0
		
        # 새로운 값들을 작은값부터 방문 
        for new_v in sorted(G[v]):
        # print(sorted(G[v])[0])
            dfs(new_v)

    return path
for tc in range(3):
    N, M, V = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)
        
	# return값이 없다 path를 여기에 미리 선언해주어야 함
    path = []
    print(dfs(V))
```



dfs는 인접한 인덱스의값이 방문된적이 없을 때, 마지막에 append된 값이 pop되어 깊이 들어갔다가 더 이상 방문하지 못한 값이 없을 때 다시 올라와서 다른 방향을 체크함.



bfs는 타겟처럼 범위로 인접한 값들부터 먼저 방문하고 방문하면서  append된 값들은 뒤로가기 때문에 중복된값들이 이미 앞에서 나왔을 시에 방문할 필요가 없어진다.

pop을 앞쪽에서 실시한다.



## #18429_근손실 



중량 증가량 리스트에 대한 숫자들의 순열을 모두 검증해야한다.

테스트케이스에서 3 7 5 는 375 357 735 753 537 573이고 3으로 시작할때 중량이 500미만이 되므로 조건을 만족하지 못한다.

총 6개의 순열중 4개만 만족한다.

dfs로 풀이가 가능하다.

```python
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            # 2.짝수 자리일때 첫번째와 세번째를 교체(312) 4.첫셋교체 (231)
       
            if i % 2 ==0:
                arr[0], arr[i] = arr[i], arr[0]
           # 1. 첫번째수와 두번째 수를 교체(213) 3. 첫둘교체 (132) 5.첫둘교체(312)
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
```

순열을 출력하는 코드

123 213 312         12바꾸고 23바꾸고

132 231 321		12바꾸고 23바꾸고 12바꾸고

```python
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")

# 순열구하는 패키지 함수코드
```



```python
# 순열 구하고 차례로 무게라는 매개변수에 더한다음 4를 빼서 0보다 작다면 답에 포함시키지 않는다.

from itertools import permutations
n, k = map(int, input().split())

arr = list(map(int, input().split()))
answer = 0
for data in permutations(arr, n):
    # print(data)
    weight = 0
    track = True
    for i in range(n):
        weight += data[i]
        weight -= 4
        if weight < 0:
            track = False
            break
    if track:
        answer += 1

print(answer)
```





## 11399_ATM

https://www.acmicpc.net/problem/11399

숫자들을 오름차순으로 정렬해주고

각 인덱스의 길이만큼을 앞에서 부터 더한 다음 그 더해진 값들의 총합을 구하는 문제이다.



```python
N = int(input())
atm = list(map(int,input().split()))

for i in range(N-1):
    for j in range(N-1):
        if atm[j+1] < atm[j]:
            atm[j+1], atm[j] = atm[j], atm[j+1]

total = 0
for i in range(N):
    for j in range(i+1):
        total += atm[j]
print(total)
```





## 16953_AtoB

https://www.acmicpc.net/problem/16953



첫번째 숫자에 2를 곱하거나 마지막 자리에 1을 추가하여 두번째 숫자가 되게 만드는 문제다.

dfs, bfs 스택, 큐 로 접근이 가능하다.



같은 값이면 멈추고 그렇지 않으면서 계산 후의 결과가 두번째 값보다 작다면 해당 계산을 진행하여준다.



```python
while que:
	...
if i*2<= b:
    que.append(i*2, cnt+1)
if int(str(i)+'1') <= b:
    que.append((int(str(i)+'1'), cnt+1))


```



큐스택을 쓰지 않고 while 조건문으로 해결 가능하다.

거꾸로 생각해야한다.

두번째 숫자의 마지막 자리수가 1이거나 2로 나누어떨어진다면 해당 계산을 진행하여준다. (단 전자의 조건을 먼저 주기)

만약 두개의 케이스 모두 해당되지 않는다거나 첫번째 숫자보다 작아진다면 실패한 것으로 break로 반복문에서 빠져나와 -1 값을 출력시켜준다.

```python
a, b = map(int, input().split())

cnt = 0

while True:
    if a == b:
        cnt += 1
        break
    elif (b % 10 != 1 and b % 2 != 0) or b < a:
        cnt = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            b //= 2
            cnt += 1

print(cnt)
```





## 12871_무한문자열

https://www.acmicpc.net/problem/12871

ab

abab 는 같으니 1

abc

bca는 반복해도 abcabc bcabca이므로 다르다 그러니 0을 출력



작은 문자열이 반복해서 길이가 더 긴 문자열이 될 수 있는지 봐주면 된다.



그냥 길이가 긴 문자열에서 짧은 문자열로 나눠 

짧은 문자열 * 나눈 배수를 해서 비교해주면 7글자 2글자 같은 경우 3.5 이런식으로 곱하기 때문에 비교가 불가능하다.

따라서 나누어 떨어지지 않는다면 최소 공배수를 구해서 각 문자열에 그만큼 곱해준 다음 둘을 비교해서 같으면 1 , 다르면 0을 출력해주면 된다.

```python
s = input()
t = input()
words_len = len(s) * len(t)
ls = int(words_len / len(s))
if s * len(t) == t * len(s):
    print(1)
else:
    print(0)

```





## #14889_스타트와링크

S3

https://www.acmicpc.net/problem/14889



| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :---- | :-------- | :-------- |
| 2 초      | 512 MB      | 39187 | 20098 | 11666     | 48.117%   |

 문제

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

| i\j  | 1    | 2    | 3    | 4    |
| :--- | :--- | :--- | :--- | :--- |
| 1    |      | 1    | 2    | 3    |
| 2    | 4    |      | 5    | 6    |
| 3    | 7    | 1    |      | 2    |
| 4    | 3    | 4    | 5    |      |

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S12 + S21 = 1 + 4 = 5
- 링크 팀: S34 + S43 = 2 + 5 = 7

1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S13 + S31 = 2 + 7 = 9
- 링크 팀: S24 + S42 = 6 + 4 = 10

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력

첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력

첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.



 예제 입력 

```
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
```

 예제 출력 

```
0
```



![image-20210421214111217](C:\Users\a\알고리즘\.Baekjoon\baekjoon.README.assets\image-20210421214111217.png)



팀 배정을 위한 선수들을 선택하고 인덱스값을 바꿔가며  체크했다 지웠다 하는게 어려웠습니다.

종료조건이나 갱신하는 것은 다른 swea 문제들과 비슷했습니다.

인덱스와 카운팅값을 갖고 놀고 싶네요..



(다른 답을 보다가 둘의 차이가 0이 나왔을 때 바로 print하고 sys.exit()한 코드를 참고해서 적용시켰더니 0.3초 단축되었습니다..ㅎ)



```python
# 1. 능력치 차이의 최소를 찾는 함수 실행
def solution(idx, cnt):
    global smallest
    # n까지 오면 인덱스 초과
    if idx == n:
        return
    # 반으로 팀이 나뉘었을 때 팀별 스탯의 차를 구함
    if cnt == n//2:
        s1, s2 = 0, 0
        for i in range(n):
            for j in range(n):
                # 1으로 된 팀
                if check[i] and check[j]:
                    s1 += stat[i][j]
                # 0으로 된 팀
                elif not check[i] and not check[j]:
                    s2 += stat[i][j]
        # 기존보다 작으면 최소값 갱신
        if smallest > abs(s1-s2):
            smallest = abs(s1-s2)
        return

    # 선택
    check[idx] = 1
    # 다음값 탐색
    solution(idx+1, cnt+1)
    # 탐색 후 리셋
    check[idx] = 0
    # 다음 인덱스를 선택하기 위해서 인덱스만 올려주기
    solution(idx+1, cnt)


# n명의 선수
n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
# 팀을 구분하기 위한 리스트
check = [0]*n
smallest = 9999
# 1. 능력치 차이의 최소를 찾는 함수 실행
solution(0, 0)
# 2. 결과값 출력
print(smallest)
```





## #2667_단지번호붙이기

S1

https://www.acmicpc.net/problem/2667



| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :---- | :-------- | :-------- |
| 1 초      | 128 MB      | 81045 | 33210 | 21005     | 39.131%   |

 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)

 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

 예제 입력 1 

```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

예제 출력 1 

```
3
7
8
9
```

문제를 추천받아 오랜만에 bfs를 시도해보았다.

큐를 사용하는게 기억이 잘 안났고 deque는 처음 써보았다.

딕셔너리의 값들을 오름차순으로 정렬하라고 문제에 써있었는데 이거 때문에 한참 수정했다..

deque에 원소를 삽입할 때도 왜 이중리스트로 담아야 하는지 이해가 잘 안갔는데, 델타이동에서 행과 열의 인덱스를 꺼내야 할 때  queue에서 pop 한거의 좌우를 나눠주어야 해서 그렇다. 

만약 리스트 하나로 감싸면 리스트가 아닌 숫자에서 숫자를 꺼내는 꼴이다..!



```python
# 3. 지도 범위 내인지 확인 
def is_safe(c, r):
    if 0 <= c < n and 0 <= r < n:
        return 1
    else:
        return 0


# 2. deque는 queue 보다 찾는 속도가 빠르다 양끝에 원소가 있을때 걸리는 시간복잡도가 n 이아니라 1임. 
def bfs(c, r, idx):
    # 이중리스트로 감싸주어야 아래 node가 리스트 식으로 나와 node[i]에서 c와 r값을 꺼낼 수 있다.
    q = deque([[c, r]])
    visited[c][r] = 1

    while q:
        # 선입선출 
        node = q.popleft()
        # 상하좌우로 살펴줌 
        for dir in range(4):
            nc = node[0] + dc[dir]
            nr = node[1] + dr[dir]
            # 범위내에 있고 방문한적없고 1이라면 queue에 삽입 
            if is_safe(nc, nr):
                if smap[nc][nr] == 1 and visited[nc][nr] == 0:
                    q.append([nc, nr])
                    # 방문체크 
                    visited[nc][nr] = 1
                    # 크기 증가 
                    house[idx] += 1


# T = int(input())
# for tc in range(1, T+1):
n = int(input())
# 0. n*n 지도 
smap = [list(map(int, input())) for _ in range(n)]
# 방문을 체크해줄 리스트
visited = [[0]*n for _ in range(n)]
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
# 키 벨류값을 담을 딕셔너리 
house = {}
idx = 0
# 1. 순회를 돌며 방문하지 않았고 값이 1인 원소들을 찾음 
for i in range(n):
    for j in range(n):
        if smap[i][j] and visited[i][j] == 0:
            # 딕셔너리에 0번부터 벨류값의 초기치를 1로하고
            house[idx] = 1
            # 2. bfs 함수를 돌며 1을 추가로 발견할 때 마다 값을 더함 
            bfs(i, j, idx)
            # 키 값 이동 
            idx += 1

# 4. 오름차순 정렬해야함 (이거 안해서 계속 틀림) 
house = sorted(house.values())
# 5. 길이와 집단크기 오름차순으로 출력
print(len(house))
for i in house:
    print(i)
```



## #18352_특정거리의 도시찾기

- https://www.acmicpc.net/problem/18352



- 다익스트라를 학습하려고 하였는데 bfs를 사용하게 되었습니다..

```python
def group_word(word):
    n = len(word)
    # group_cnt = 0
    emp = {}
    for i in range(n):
        if word[i] not in emp:
            emp[word[i]] = 1
        else:
            if word[i-1] != word[i]:
                # print('no')
                return False
            else:
                emp[word[i]] += 1
    return True

T = int(input())

cnt = 0
for _ in range(T):
    word = input()
    cnt += group_word(word)

print(cnt)


#     n = len(word)
#     group_cnt = 0
#     emp = {}
#     # for i in word:
#     for i in range(n):
#         if word[i] not in emp:
#             emp[word[i]] = 1
#         else:
#             if word[i-1] != word[i]:
#                 print('no')
#                 break
#             else:
#                 emp[word[i]] += 1
#     print(emp)
#
```





## #1719_택배





- **Reference** :
  - https://www.acmicpc.net/problem/1719





- **어려웠던 점**:
  - dijkstra 쉬운문제 연습하고 싶었는데 전혀 쉽지 않았다.
  - n이 최대 200이여서 플로이드 와샬로 풀 수 있지만 다익스트라 연습해보고 싶었다.
  - 우선순위 큐 이용해서 최단거리 그래프만 구하는거 뿐만 아니라 최단경로로 오기 전 경로를 저장하는 리스트를 만들어야 했다.
  - 또한 경로 리스트를 그대로 출력하면 안되고 시작 idx에서 가장 가까운 지점을 출력해야 해서,
  - 시작 집하장과 현재 집하장이 같아 질 때 까지 거슬러 올라간 다음에 그 거슬러 올라가기 직전 지점을 출력해야 한다.

결론은 그냥 어려웠다..
(다른 풀이들 참고한 코드입니다 :) )



```python
# import sys
from heapq import heappush, heappop
# sys.stdin = open('input.txt')


# 1-1. heapq로 우선순위 큐 구현
def Dijkstra(K, graph, V):
    heap = []
    # 거리정보
    distance = [1e9] * (V + 1)
    distance[K] = 0
    # 최단거리로 오기 전 경로를 저장
    cource = [0] * (V + 1)
    heappush(heap, (0, K))

    # 우선순위 큐
    while heap:
        weight, location = heappop(heap)

        if distance[location] < weight:
            continue

        for l, w in graph[location]:
            w += weight
            if w < distance[l]:
                distance[l] = w
                cource[l] = location
                heappush(heap, (w, l))
    return cource


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

# 0. 양방향 그래프 만들기
for _ in range(E):
    st, ed, w = map(int, input().split())
    graph[st].append([ed, w])
    graph[ed].append([st, w])

# 1. 인덱스 1부터 V개까지 다익스트라 알고리즘 실행
for idx in range(1, V+1):
    # 1-2. 실행 후 최단거리를 만들어 준 전 경로를 course에 저장
    course = Dijkstra(idx, graph, V)

    ret = ['-'] * (V + 1)

    # 2. 현재 집하장과 탐색 시작점이 같으면 자기 자신이므로 - 출력
    for jdx in range(1, V + 1):
        if idx == jdx:
            continue
        checkIndex = jdx

        # 2-1. 시작 집하장이 나올 때까지 반복한다
        while 1:
            kdx = course[checkIndex]
            # 시작 집하장 나오면 끝
            if kdx == idx:
                ret[jdx] = checkIndex
                break
            # 전 경로로 올라가기
            checkIndex = kdx
    # 3. 결과 한 줄씩 출력
    for i in range(1, V + 1):
        print(ret[i], end=' ')
    print()



```



 c++  플로이드-와샬 풀이

```c++
# c++
include <cstdio>
int N,M,dist[201][201],inf=9e8,path[201][201];
int main(){
    scanf("%d%d",&N,&M);
    for(int i=1;i<=N;i++)
        for(int j=1;j<=N;j++) {
            dist[i][j]=inf;
            if(i==j) dist[i][j]=0;
        }
    while(M--){
        int a,b,c;
        scanf("%d%d%d",&a,&b,&c);
        dist[a][b]=dist[b][a]=c;
        path[a][b]=b;
        path[b][a]=a;
    }
    for(int k=1;k<=N;k++)
        for(int i=1;i<=N;i++)
            for(int j=1;j<=N;j++) {
                if(dist[i][j] > dist[i][k]+dist[k][j]){
                   dist[i][j] = dist[i][k]+dist[k][j];
                   if(i!=k) path[i][j] = path[i][k];
                }
            }
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++) {
            if(path[i][j]) printf("%d ",path[i][j]);
            else printf("%c ",'-');
        }
        puts("");
    }
}

```





## #1593_문자해독



https://www.acmicpc.net/problem/1593



 **문제**

마야 문자를 해독하는 일은 예상 외로 어려운 일이다. 현재에도 뜻이 완전히 밝혀진 마야 문자는 거의 없는 실정이며, 그나마 해독에 진척이 시작된 지는 30여 년도 되지 않았다.

마야 문자는 소리를 나타내는 여러 종류의 그림글자로 구성되는데, 이 글자들이 여러 위치에서 결합함으로써 단어를 형성한다.

마야 문자 해독을 어렵게 하는 요인 중 하나는 바로 단어를 읽는 순서이다. 마야 문자를 쓰는 고대인들은 단어를 기록할 때 특정한 규칙 대신, 그들이 보기에 좋게 보이도록 단어를 이루는 글자들을 아무렇게나 배열했다. 그렇기 때문에 고고학자들이 마야 기록에서 단어를 이루는 각 그림글자들의 발음을 알아내더라도 그 단어를 실제로 발음하는 방법은 정확히 알 수 없는 셈이다.

고고학자들은 W라는 특정 단어를 발굴 기록으로부터 찾고 있다. 그 단어를 구성하는 각 글자들은 무엇인지 알고 있지만, 이것이 고대 기록에 어떤 형태로 숨어 있는지는 다 알지 못한다.

W를 이루고 있는 g개의 그림문자와, 연구 대상인 벽화에 기록된 마야 문자열 S가 주어졌을 때, 단어 W가 마야 문자열 S에 들어있을 수 있는 모든 가짓수를 계산하는 프로그램을 작성하시오. 즉, 문자열 S안에서 문자열 W의 순열 중 하나가 부분 문자열로 들어있는 모든 경우의 수를 계산하라는 뜻이다.

 **입력**

첫째 줄에 고고학자들이 찾고자 하는 단어 W의 길이 g와 발굴된 벽화에서 추출한 문자열 S의 길이 |S|가 빈 칸을 사이에 두고 주어진다. (1≤g≤3000, g≤|S|≤3,000,000) 둘째 줄에 W, 셋째 줄에 S의 실제 내용이 들어있다. 모든 문자열은 알파벳으로 이루어지며, 대소문자를 구분한다.

**출력**

첫째 줄에 W의 순열이 S 안에 있을 수 있는 형태의 개수를 출력한다.

 **예제 입력 1** 

```
4 11
cAda
AbrAcadAbRa
```

 **예제 출력 1** 

```
2
```



```python
# 2. 순열 구하는 함수
def perm(idx, length):
    global word, cnt
    if idx == length:
        # 미리 구해놓은 긴 문자열에 있는 단어라면 cnt 더하기 
       if ''.join(word) in s_list:
           cnt += 1

    else:
        for change in range(idx, length):
            word[change], word[idx] = word[idx], word[change]
            perm(idx+1, length)
            word[idx], word[change] = word[change], word[idx]
        
            
# 0. 입력값을 받는다.
n, m = map(int, input().split())
word = list(input())
s = list(input())
arr = [i for i in range(n)]
cnt = 0
# 1. 구간을 나눠서 n의 길이만큼 빈 문자열에 저장해준다
s_list = []
for i in range(m-n+1):
    s_list.append(''.join(s[i:i+n]))
# 2. 순열 구하는 함수 실행
perm(0, n)
# 3. 개수 출력 
print(cnt)


```

답은 맞지만 시간초과가 난다.



```python
# import sys

n, m = map(int, input().split())
g = input()
s = input()
glit =[0]*52
slit =[0]*52

for i in range(n): #glit에 알파벳에 맞게 숫자 카운팅
    if ord("a") <= ord(g[i]) and ord(g[i]) <= ord("z"):
        glit[ord(g[i])-ord('a')] += 1
    else:
        glit[ord(g[i])-ord('A')+26] += 1

for i in range(n):#s중에서 n개만큼만 선택
    if ord("a") <= ord(s[i]) and ord(s[i]) <= ord("z"):
        slit[ord(s[i])-ord('a')] += 1
    else:
        slit[ord(s[i])-ord('A')+26] += 1
cnt = 0
for i in range(m-n+1):
    fail = False
    for j in range(52):
        if glit[j] != slit[j]:
            fail = True
            break
    if fail == False:
        cnt += 1
    if i == m-n:
        break

    pos =0
    if ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z'):
        pos = ord(s[i])-ord('a')
    else:
        pos = ord(s[i])-ord("A")+26
    slit[pos] -= 1

    if ord('a') <= ord(s[i+n]) and ord(s[i+n]) <= ord('z'):
        pos = ord(s[i+n])-ord('a')
    else:
        pos = ord(s[i+n])-ord("A")+26
    slit[pos] += 1

print(cnt, end="")
```

문제의 첫부분을 잘 해석해보면  아스키코드를 이용하라는 내용이 나온다.

아스키 코드값을 사용해야 정해진 시간안에 해결이 가능하다..

