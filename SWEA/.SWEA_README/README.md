# SWEA 문제풀이 ​ ​ ​ ​ :smiley:  :slightly_smiling_face: ​ :sweat: ​ :face_with_head_bandage:

## 0217 수

***

### After class:rose:

HW GNS

list2 4문제

백준 1솔이상

그래비티

스트링복습



## 1221_GNS

d3

문자열로 된 리스트를 숫자로 변환해주고 정렬한 리스트로 만들고 그 숫자들을 문자열로 변환해주는 리스트를 작성할 것임



```python
def str_int(x):
    emp = []
    for i in x:
        if i == 'ZRO':
            i = 0

        elif i == 'ONE':
            i = 1
        elif i == 'TWO':
            i = 2
        elif i == 'THR':
            i = 3
        elif i == 'FOR':
            i = 4
        elif i == 'FIV':
            i = 5
        emp += [i]

    for i in range(len(emp)-1, -1, -1):
        for j in range(i):
            if emp[j] > emp[j+1]:
                emp[j+1], emp[j] = emp[j], emp[j+1]
    return emp

print(str_int(prac_list))
```

문자열을 숫자로 변경하고 정렬하는거까지 해줌

```python
    emp2 = []
    for i in emp:
        if i == 0:
            i = 'ZRO'
        elif i == 1:
            i = 'ONE'
        elif i == 2:
            i = "TWO"
        elif i == 3:
            i = "THR"
        elif i == 4:
            i = "FOR"
        elif i == 5:
            i = "FIV"
        emp2 += [i]
    return emp2
```

위 함수에 이 식을 추가하여 코드 함수로 코드를 완성함

![image-20210217235721606](C:\Users\a\Desktop\typora\aidenrism_daily\SWEA_README\README.assets\image-20210217235721606.png)

*앞에써주면 공백이 생김



```python
T = int(input())
 
for tc in range(1, T+1):
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
    N = list(map(str, input().split()))
    string = list(map(str, input().split()))
    bin = []
 
    for i in range(10):
        for j in string:
            if j == num[i]:
                bin.append(j)
 
    print(N[0])
    print(*bin)
```



num의 숫자에 따라 앞에 쌓이므로 이렇게 간단한  코드도 있었다..

``` python
T = int(input())
mars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
for tc in range(1, T+1):
    count = [0] * 10
    n = int(input()[3:])
    mars_num = input().split()
 
    for num in mars_num:
        idx = mars.index(num)
        count[idx] += 1
 
    result = []
    for i in range(10):
        result += [mars[i]] * count[i]
 
    result = ' '.join(result)
    print('#{}\n{}'.format(tc, result))
```

조금 변형된 코드



## 0218 목



## #4864_문자열비교 

(y)

첫줄의 문자열이 두번째줄의 문자열에 있으면 1출력 없으면 0 출력

 **패턴매칭**이다 



## #5432_쇠막대기 자르기

d4

2' 손으로 그려본 결과 () ((( () () ) ( () ) () )) ( () )  

'('다음에 바로 ')' 닫는 괄호가오면 레이저이고 여는 괄호 '(' 뒤에 '('가 온다면 막대 시작 

닫는괄호 ')' 앞에 ')'가 있다면 막대기의 닫히는 부분이다.



그리고 레이저 앞에 여는괄호 개수에 따라서 그 해당 레이저가 만드는 잘려진 막대기 개수를 구할 수 있고 닫히는 괄호도 마찬가지로 앞의 레이저가 몇개나 자를 수 있는지 구할 수 있게 해준다.

()가 나타난다면 앞의 괄호 개수를 계산하여야 한다.

<>>기존 

```python
    if pipe[i+1] == pipe[i] and pipe[i] == '(':
        cnt += 1
    elif pipe[i-1] == pipe[i] and pipe[i] == ')':
        cnt -= 1
    if pipe[i] != pipe[i+1] and pipe[i] == '(':
        emp.append(cnt)
```

자신이 ( 고 뒤에도 자신과 같다면 +=1 

자신이 ) 고 자신의 앞에도 자신과 같다면 -=1  

자신이 ( 고 자신의 뒤에가 자신과 다르다면 그때의 cnt를 빈 리스트에 append

자신이 ) 고 자신의 앞이 자신과 다르고 뒤에가 자신과 같으면, 그때 (가 나오기 전까지의 자신의 뒤에 ) 개수를 세어준다

```python
T = int(input())

for tc in range(1, T+1):
    pipe = input()
    cnt = 0
    emp = []
    # i+1까지 비교해야하므로 len -1
    for i in range(len(pipe) - 1):
        if pipe[i+1] == pipe[i] and pipe[i] == '(':
            cnt += 1
        elif pipe[i-1] == pipe[i] and pipe[i] == ')':
            cnt -= 1
        if pipe[i] != pipe[i+1] and pipe[i] == '(':
            emp.append(cnt)
        if pipe[i-1] != pipe[i] and pipe[i] == ')':
            back_cnt = 0
			# 뒤의  ) 개수 세주기 
            for j in range(1, len(pipe)-i):
                if pipe[i+j] == ')':
                    back_cnt += 1
                else:
                    break
            emp.append(back_cnt)
	# sum 값 출력 
    emp_cnt = 0
    for k in range(len(emp)):
                emp_cnt += emp[k]
    print('#{} {}'.format(tc, emp_cnt))

```



```python
T = int(input())
for tc in range(1, T + 1):
    tem = input()
    lst = []
    for i in range(len(tem)):
        if tem[i] == "(" and tem[i + 1] == ")":
            lst.append(0)
        elif tem[i] == ")" and tem[i - 1] != "(":
            lst.append(-1)
        elif tem[i] == "(":
            lst.append(1)
    print(lst)
    print(tem)
    # -1을 앞에서 부터 찾은 이후, 다시 돌아가서 가장 먼저 있는 1을 찾고, 그 안에 들어있는 별을 찾기
    total_star = 0
    for i in range(len(lst)):
        tem_sum = 0
        star = 0
        for j in range(len(lst) - i):  # i + j = len()까지 구할거임
            if lst[i] == 0:
                break
            elif lst[i] == -1:
                break
            elif lst[i] == 1:
                if lst[i + j] == 1:
                    tem_sum += 1
                elif lst[i + j] == 0:
                    star += 1
                elif lst[i + j] == -1:
                    tem_sum -= 1
                    if tem_sum == 0:
                        break
        if star != 0:
            total_star += star + 1
    print('#{} {}'.format(tc, total_star))
```

실행시간이 초과나지만 이런코드도 있었다.



```python
def solution(string):
    lasers = []
    sticks = []

    for idx in range(len(string)):
        if string[idx] == '(':
            # laser?
            if string[idx+1] == ')':
                lasers.append((idx, idx+1))
            else:
                n = 0
                for j in range(idx, len(string)):
                    n = n + 1 if string[j] == '(' else n - 1
                    if n == 0:
                        sticks.append((idx, j))
                        break

    result = len(sticks)
    for stick in sticks:
        for laser in lasers:
            if stick[0] < laser[0] and stick[1] > laser[1]:
                result += 1
                
    # print(laser, sticks)
    return result
T = int(input())

for tc in range(1, T+1):
    print("#{} {}".format(tc, solution(input())))
```

 출력결과:

(19, 20) [(2, 17), (3, 16), (4, 9), (10, 13), (18, 21)]
#1 17
(23, 24) [(0, 19), (1, 18), (2, 11), (5, 10), (12, 15), (20, 25)]
#2 24

스틱의 개수를 구해주고 레이저로 쏠 때마다 스틱들을 한개씩 더해주는 방법



