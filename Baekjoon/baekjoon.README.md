



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