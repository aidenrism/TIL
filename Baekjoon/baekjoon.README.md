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

