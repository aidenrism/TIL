

# SWEA 문제풀이 ​ ​ ​ ​ :smiley:  :slightly_smiling_face: ​ :sweat: ​ :face_with_head_bandage:

## 0217 수

***

### :rose:

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

0.5)



첫줄의 문자열이 두번째줄의 문자열에 있으면 1출력 없으면 0 출력

 **패턴매칭**이다 



한칸씩 이동하면서 짧은 단어의 길이만큼 비교해주는 코드로 작성하였다.



```python
T = int(input())

# 값을 받아드리고 길이를 구한다.
for tc in range(1, T+1):
    short = input()
    long  = input()

    n = len(long)
    m = len(short)

    # 시작점을 움직여주면서 값을 비교해본다. 
    st = 0
    cnt = 0
    while st < n - m + 1:
        if long[st:st + m] == short:
            st += m
            cnt += 1
        elif long[st:st + m] != short:
            st += 1
    # 같은 값을 발견하여 카운트가 올라갔다면 compare 변수를 1로 만들어준다.
    if cnt > 0:
        compare = 1
    else:
        compare = 0

    print('#{} {}'.format(tc, compare))

```



두번째는 함수를 만들어서 바로 함수에 적용시켜 출력하여 주었다.

```python
# 짧은 단어와 긴 단어를 받아서 두개의 길이를 구하는 함수를 만든다.
def compare(short, long):
    m = len(short)
    n = len(long)
    st = 0
    # 구간을 비교할 때 쓰는 n-m+1을 이용하여 짧은 단어의 길이만큼 반복해서 비교해본다.
    while st < n-m+1:
        if long[st:st+m] == short:
            return 1
        else:
            st += 1
    return 0

T = int(input())

# 값을 받아드려 출력시에 함수에 적용하여 출력한다.
for tc in range(1, T+1):
    short = input()
    long  = input()

    print('#{} {}'.format(tc, compare(short, long)))
```



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



## #4836_색칠하기

*2.5*



2 2 4 4 1 

3 3 6 6 2

마지막이 1이면 red, 2이면 blue 컬러이다.

10*10 빈 리스트를 만들어 red면 1을 만들어주고 그 자리에 블루가 온다면 2를 만들어

2의 개수를 세주면 전체 보라색 넓이의 크기를 알 수 있을 것이다.

```python
n = int(input())

for _ in range(n):
    square = list(map(int, input().split()))
    paper = [[0] * 10 for _ in range(10)]
    if square[-1] == 1:
        color = 'red'
    else:
        color = 'blue'

    for i in range(square[0], square[2]+1):
        for j in range(square[1], square[3]+1):
            paper[i][j] = 1
            # print(i, j)
    print(color)
    cnt = 0
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] == 1:
                cnt += 1
    print(cnt)
```

이렇게 빨강과 파랑 넓이를 알 수 있었다.



```python
# 테스트 케이스 개수 입력
T = int(input())
for tc in range(1, T+1):
    # 사각형의 개수 입력
    n = int(input())
    # 백지 생성
    paper = [[0] * 10 for _ in range(10)]
    cnt = 0
    for num in range(n):
        square_num = list(map(int, input().split()))
        # 빨강색에 해당되는 인덱스는 백지에 1로 표시
        if square_num[-1] == 1:
            color = 'red'
            for i in range(square_num[0], square_num[2] + 1):
                for j in range(square_num[1], square_num[3] + 1):
                    paper[i][j] = 1
        # 파란색은 빨강색이 있을 때 1을 더해준다
        else:
            color = 'blue'
            for i in range(square_num[0], square_num[2] + 1):
                for j in range(square_num[1], square_num[3] + 1):
                    if paper[i][j] == 1:
                        paper[i][j] += 1

                # print(i, j)
        # print(color)
        # 2인거의 개수를 세기 
        for i in range(len(paper)):
            for j in range(len(paper)):
                if paper[i][j] == 2:
                    cnt += 1
    
    print('#{} {}'.format(tc, cnt))
```

이렇게 하면 10개중 4개만 맞아서 fail이다. 파란색에 += 1 이 아니라 2로 만들어주고 시도해보자.

다른게 문제가 아니라 cnt 초기화 위치가 문제였다.

```python
# 테스트 케이스 개수 입력
T = int(input())
for tc in range(1, T+1):
    # 사각형의 개수 입력
    n = int(input())
    # 백지 생성
    paper = [[0] * 10 for _ in range(10)]

    for num in range(n):
        square_num = list(map(int, input().split()))
        # 빨강색에 해당되는 인덱스는 백지에 1로 표시
        if square_num[-1] == 1:
            # color = 'red'
            for i in range(square_num[0], square_num[2] + 1):
                for j in range(square_num[1], square_num[3] + 1):
                    if paper[i][j] == 0:
                        paper[i][j] = 1
                    elif paper[i][j] == 2:
                        paper[i][j] = 3
                    # elif paper[i][j] == 3:
                    #     paper[i][j] = 4

        # 파란색은 빨강색이 있을 때 1을 더해준다
        elif square_num[-1] == 2:
            # color = 'blue'
            for i in range(square_num[0], square_num[2] + 1):
                for j in range(square_num[1], square_num[3] + 1):
                    if paper[i][j] == 1:
                        paper[i][j] = 3
                    elif paper[i][j] == 0:
                        paper[i][j] = 2
                    # elif paper[i][j] == 3:
                    #     paper[i][j] = 4
                # print(i, j)
        # print(color)
        # 2인거의 개수를 세기
        cnt = 0 # cnt를 여기서 초기화해주지않고 위에서 초기화해서 계속 실패하였다..
        for i in range(len(paper)):
            for j in range(len(paper)):
                if paper[i][j] == 3:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))
```



## #4861_순회

1) :slightly_smiling_face: 

word[m-1+j : j-1 : -1] 거꾸로 불러오는 슬라이싱에서 헤매어서 시간이 오래걸렸다.

그래서 for문으로 거꾸로 알파벳을 받아와서 단어를 만드는 reverse_word를 만들었다.

```python
# 순회를 돌릴단어와 원하는 크기의 값을 num으로 주어 num의 값에 해당하는 순회 단어를 불러온다.
def my_palindrome(word, num):
    # print(word, num, len(word))
    n = len(word)
    m = num
    for j in range(n-m+1):
        reverse_word = ''
        for k in range(m-1+j, j-1, -1):
            reverse_word += word[k]
        # print(reverse_word, 1)
        if word[j:j+m] == reverse_word:
            return word[j:j+m]

# 테스트케이스를 받는다 
T = int(input())

for tc in range(1, T+1):
    # 전체 글자판의 폭과 순회문의 원하는 길이를 입력받는다.
    n, m = map(int, input().split())
	
    # 2차원 리스트를 만든다.
    sentences = [input() for _ in range(n)]
    # print(sentences)
    
    # 순회에 해당될 시 결과에 저장할 임시 str이다.
    output = ''
	# 우선 가로로 확인한다.
    for i in range(n):
        result = my_palindrome(sentences[i], m)
        if result:
            output += result

	# 세로로도 확인한다.
    for i in range(n):
        col_sentence = ''
        # 세로로 알파벳을 더해 세로줄 단어를 만들어준다.
        for j in range(n):
            col_sentence += sentences[j][i]
        result2 = my_palindrome(col_sentence, m)
        if result2:
            output += result2
    # 결과 출력 
    print(output)

```



72퍼 66퍼 14시간  (1시간)



## #4873_부분집합의 합

1.5)

:sweat:

```python
num = [1,2,3,4,5,6,7,8,9,10,11,12]
Len = len(num)

#부분집합 구하기
lst = []
# 2**12 만큼 i를 생성
for i in range(1<<Len):
    # 부분집합을 받을 리스트
    sub_lst = []
    # 1을 0~12번 시프팅해가며 i와 j번째 비트가 1인지 아닌지 리턴
    for j in range(Len):
        if i & (1<<j):
            sub_lst.append(num[j])
    lst.append(sub_lst)
# 2의 12승인 4096만큼 부분집합을 만듦
# print(lst)

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())

    k_lst = []
    for idx in lst:
        if len(idx) == n:
            k_lst.append(idx)
    # 부분집합의 길이가 n개인 리스트들
    # print(k_lst)

    result = 0
    # 부분집합의 합이 k면 result에 1을 더해줌
    for kdx in k_lst:
        if sum(kdx) == k:
            result += 1
    print('#{} {}'.format(tc, result))
```

부분집합의 생성을 어떻게 할 지에 대하여 생각하는게 너무 어려웠다.

시프트와 엔드에 개념이 잘 잡혀있지 않아서 그런것 같다. 

1~12의 부분집합을 만드는거니 1<<12 로 2의 12승만큼 (1을 12번 시프트한것의 개수만큼) i를 만들고 j를 0~11 총 12번 1의 시프팅에 변화를 주어 해당되는 값에 i가 존재한다면 그 값을 부분집합으로 만들어준다.

말하면서도 쉽게 설명이 어려운 개념같다. (나도 아직 완벽하게 숙지되어있지 않은것 같은 느낌)

j가 0이면 1을 0번 시프팅. 즉 1의 자리에 해당되는 i값들을 찾아옴.

j가 1이면 1을 2의 1승만큼 시프팅. 2진수 2번째 자리 값들을 가져옴. 



## #2005_파스칼 삼각형

2)

재귀호출.. 잘 모르겠다.

i 그대로 밑으로가고 



```python
T = int(input())

for tc in range(1, T + 1):

    num = int(input())
    print('#{}'.format(tc))
    # N은 10이하의 정수 -- 2차원 리스트 생성
    s = [[0 for _ in range(10)] for _ in range(10)]

    # 양 끝에 1을 주고 안쪽에는 왼쪽위와 자신의 위의 값을 더해주기
    for i in range(0, num):
        for j in range(0, i + 1):
            if j == 0 or i == j:
                s[i][j] = 1
            else:
                s[i][j] = s[i - 1][j - 1] + s[i - 1][j]

    # 0이 아닌값들 출력해주기
    for i in range(0, num):
        for j in range(0, num):
            if s[i][j] == 0:
                print('', end='')
            else:
                print(s[i][j], end='')
        print('')
```

테스트케이스 10개중 7개 pass



다음은 구글링해서 찾은 것인데 내일 다시 기억해서 써볼 예정이다.

```python
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    result = [[1]]

    for i in range(1, N):
        row = [1]
        for j in range(len(result[-1])-1):
            sumV = 0
            for k in range(2):
                sumV += result[-1][j+k]
            row.append(sumV)
        row.append(1)
        result.append(row)

    print('#{}'.format(tc))
    for i in range(len(result)):
        print(*result[i])
```

1을 처음과 끝에 append하는 것이 깔끔해보였다.



## #4866_괄호검사

2)

 1 닫는 괄호부터 시작했을 때 #빼먹음 이거해도 tc 3 -> 4
 2 여는 괄호와 닫는 괄호의 수가 일치하지 않았을 때
 3 들어갔다가 pop할 때의 여는괄호와 닫는괄호가 다를 때

이 조건들을 만족하면 정상적인 짝을 이룬경우이고 1을 출력한다.



```python


T = int(input())

for tc in range(1, T+1):
    words = input()
    sentence = []
    opener = '({['
	closer = ')}]'
	result = 1
    for word in words:
        if word in opener:
            sentence.append(word)

        elif word in closer:
            if len(sentence) == 0:
                result = 0
            elif sentence[-1] == '(' and word == ')':
                sentence.pop()
            elif sentence[-1] == '{' and word == '}':
                sentence.pop()
            elif sentence[-1] == '[' and word == ']':
                sentence.pop()
    if len(sentence) == 0 and result:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))
```



elif word in closer:

이 부분을 if에서 elif로 고쳤을 때 tc 성공이 4개에서 8개로 늘어났다.

2 개는 뭘까..



```python
            elif word in closer:
                if len(sentence) == 0:
                    result = 0
                    break
```

break을 걸었을때 아래 len ==0 : result = 1 과 안 충돌하므로 tc통과 한개 늘어남. 9개..



```python
T = int(input())

for tc in range(1, T+1):
    words = input()
    sentence = []
    opener = '({['
    closer = ')}]'
    result = 0

    # input 값을 하나씩 추출하여 for 문을 돌린다.
    for word in words:
        # 여는 괄호면 빈 리스트에 넣어준다
        if word in opener:
            sentence.append(word)

        # 닫는 괄호면
        elif word in closer:
            # 빈 리스트가 비어있을 때 결과값을 -1
            if len(sentence) == 0:
                result = 0
                break
            # 리스트가 비어있지 않을 때 여는괄호와 같은 종류면 리스트에서 그 값을 뺀다.
            elif sentence[-1] == '(' and word == ')':
                sentence.pop()
            elif sentence[-1] == '{' and word == '}':
                sentence.pop()
            elif sentence[-1] == '[' and word == ']':
                sentence.pop()
            else:
                result = 0
        # 다 빼고 길이가 0 이면 result는 1 그리고 다시 for문의 다른 word로
        if len(sentence) == 0:
            result = 1
        else:
            result = 0
    # input값이 공백이면 result 1
    if len(words) == 0:
        result = 1
    print('#{} {}'.format(tc, result))
```

반례 못찾음.



결론:

tc에 공백은 없다

```python
           # 다 빼고 길이가 0 이면 result는 1 그리고 다시 for문의 다른 word로
            if len(sentence) == 0:
                result = 1
            else:
                result = 0
```



```python
        if len(sentence) == 0 and result :
            result = 1
        else:
            result = 0
```

들여쓰기하고 길이가 0이지만 result는 0인 값들이 result가 1이 되서 나오는것을 막아야 함.





## #4871_그래프경로

3)

노드들 사이에 방향이 있는 간선을 가지는 그래프이다.

vertex(node) : 꼭지점, edge: 간선



```python
v, e = map(int, input().split())
emp1 = []
emp2 = []
for _ in range(e):
    s, g = map(int, input().split())
    if s == 1:
        emp1.append([s,g])
    else:
        emp2.append(s)
    # if s in emp1:
    #     emp1.append(g)

print(emp1)
print(emp2)
```

[[1, 4], [1, 3]]
[2, 2, 4]

```python
for _ in range(e):
    s, g = map(int, input().split())
    sg_list = [s,g]
    print(sg_list)
```

[1, 4]
[1, 3]
[2, 3]
[2, 5]
[4, 6]



방문할지 안할지 고려할때 TF값을 고려하면 됨.



#### 새로 

1. 입력 값들을 받는다. (V, E, start, end, S, G)

2. 인접리스트를 만든다. (graph)  ex) 1번인덱스에 1이 갈 수 있는 값들.. 2번인덱스에 2가 갈 수 있는 값들..

3. T F값이 있는 visited [] 리스트와 값들을 push & pop 을 할 stack 리스트를 만든다. (stack 리스트를 to_visit으로)

4.  to_visit = [] 에 스타트값을 넣어줌 스타트값을 인접리스트에 넣고 해당되는 값을 stack에 넣어줌(5번에서tf먼저 체크하고 while  stack 값들이 존재하는 동안을 먼저 해줘야 한다..)

5.  stack에서 꺼낼 때  그 값을 current 변수로 만들어줌 .current변수를 visited 리스트에서 확인함. T인지 F인지, 인접리스트인 graph의 current에 해당되는 값들을 to_visit(스택)에 append 시킴. 

   그럼 없다면 while이 종료될것이고 (스택에 값이 없다면= 방문할 값들이 더이상없다는것), 그  때의 visited값을 보면 방문했다면 1 없다면 0 (T, F) 로 출력 가능.



```python
T = int(input())

v, e = map(int, input().split())

graph = [

]
for _ in range(e):
    start, end = list(map(int, input().split()))
    graph.append([start, end])

S, G = map(int, input().split())

print(graph)
print(S, G)
```

[[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
1 6   

1,2번 까지 함.

--> graph 잘못만듦.

start,end 를 묶어서 append 시켰는데 이렇게 하면 안되고 graph의 start 번째 인덱스에 end 값을 넣어야 함

```python
# 2차원 인접리스트의 생성
graph = [
 
]
for _ in range(e):
    start, end = list(map(int, input().split()))
    graph[start].append(end)
```

graph가 1차원이어서 에러가 난다.

```python
# 2차원 인접리스트의 생성
graph = [[] for _ in range(v+1)]
for _ in range(e):
    start, end = list(map(int, input().split()))
    graph[start].append(end)

```

[]를 노드의 개수 +1 만큼 2차원으로 만들어주어서 나중에 인덱스값 그대로 집어넣어 비교하거나 꺼내 올 수 있음.



```python
def StartToEnd(v, e, graph, S, G):

    # 값들을 stack할 리스트
    to_visit = [S]

    # 값들의 방문 여부를 확인할 리스트 (숫자를 그대로 인덱스 값으로 받으려면 노드값에 1을 더해주면 됨
    visited = [[False] for _ in range(v+1)]
```

3번까지 함



--정리 안된 코드 

```python
def StartToEnd(v, e, graph, S, G):

    # 값들을 stack할 리스트
    to_visit = [S]
    # to_visit.append(S)

    # 값들의 방문 여부를 확인할 리스트 (숫자를 그대로 인덱스 값으로 받으려면 노드값에 1을 더해주면 됨
    visited = [[False] for _ in range(v+1)]
    # for idx in to_visit:
    #     to_visit += graph[idx]
    
    while to_visit:
        current = to_visit.pop()
        if visited[current] == False:
            # print(current)
            # print(visited[1])
            visited[current] = True
            # print(visited[1])
            #
            to_visit.append(graph[current])
            print(to_visit)
    return visited[G]
```



==> 정리 된 코드 

````python
def visiting(v, graph, S, G):

    # 값들을 stack할 리스트 초기값은 출발점을 준다
    to_visit = [S]

    # 값들의 방문 여부를 확인할 리스트 (숫자를 그대로 인덱스 값으로 받으려면 노드값에 1을 더해주면 됨
    visited = [False for _ in range(v+1)]

    # 스택에 값이 있는동안 반복한다.
    while to_visit:
        # 현재 위치는 스택에서 나온값
        current = to_visit.pop()
        # 방문하지 않았다면 T로 체크해주고 거기에 해당되는 인접리스트를 스택에 append 시킨다.
        # if visited[current] == False: # 밑에와 같음
        if not visited[current]:
            visited[current] = True
            # append는 [3,4]를 리스트로 해준다 3,4만 들어가게 해줘야 에러가 안남.
            to_visit += graph[current]

    # goal의 값이 방문이 되었는지 체크하고 결과로 반환한다. true false를 숫자로 변환
    return int(visited[G])
````



이제 시작점 S를 stack에 넣고 시작한다. (stack명은 to_visit)

while문을 만들고 to_visit이라는 리스트에 값이 있을 때까지 도는 것을 설정한다.

 반복문이 도는동안 current는 현재 위치로 stack.pop을 이용하여 stack에 있는 값을 가져온다

만약 그 값이  visited 리스트의(초기는 다 False임) False라면 방문을 했으니 True로 바꿔주고 인접리스트 graph의 current번째 인덱스를 스택에 넣어준다



여기서는 시작점이자 current 가 1이므로 1의 인접리스트를 가지고 오고 그 값은 4,3이다 

이제 여기서 한 값이 pop될것이다. 

3이라고 가정하면 3은 current고 기존 F니까 T로 변환해준다 그리고 인접리스트의 3을 보면 해당 값이 없으므로 스택에 추가되는 값은 없다. 

스택에 4가 한개 남아있으므로 while 문은 돌고 ,

4는 current가 된다. 4는 방문한적이 없으므로 visited에서 F를 T로 변환해준다.

그리고 4의 인접리스트를 보면 6이 있다. 6을 스택에 넣어준다.

스택에는 6만 있다.

6은 current가 되고 방문한적이 없으므로 F에서 T로 변환해준다.

그리고 6의 인접리스트를 보면 값이 없다.

그러므로 더 이상 스택에서 뽑을 값이 없으므로 while 문이 종료되고 G에 해당되는 visited의 G번째 (방문 여부를 알 수 있는) 값이 return 된다.

6은 마지막에 방문되었으므로 True 즉 1이다.



결과: [False, True, False, True, True, False, True]
[False, False, True, True, False, True, True, False]
[False, True, False, True, False, True, False, True, True, True]



#1 1
#2 1
#3 1



## #4873_반복문자지우기

1.5)

stack 구조를 활용한다. 

마지막값을 pop 하고 남아있는 값중 마지막 값과 비교하여 일치하면 마지막 값도pop하여 제거해준다.

제거해주고 나서는 i -= 1 을 해준다 ( 단 i > 1 클 때) 

만약 다르다면 i == 1일 때만 words.insert(len(words))를 해주고

i > 1 words.insert(-i+1) 을 해줘서 다시 제자리에 집어 넣는다.

다를 때는 항상 i += 1을 해준다.



@만약 i가 words길이보다 크거나 같으면 break로 멈춰준다.

```python
T = int(input())

for tc in range(1, T+1):
    words = list(input())
    i = 1
    
    while len(words) > 1:
        if i >= len(words):
            break
        # 마지막 stack 값을 추출하고 그 전에 값과 비교한다
        current = words.pop(-i)
        if words[-i] == current:
            words.pop(-i)
            if i > 1:
                # 일치하여 뽑았다면 다시 그 전의 값과 다음값을 비교해본다.
                i -= 1
        # 마지막 stack 값과 다르다면 다시 제자리에 word를 집어넣어주고 그 아래값을 pop한다.
        else:
            if i == 1:
                words.insert(len(words), current)
            else:
                words.insert(-i+1,current)
            # 값을 추출하지 못했으므로 하나 더 아래 stack의 값을 살펴봄
            i += 1
    print('#{} {}'.format(tc, len(words)))
```



## #1219_길찾기

1) 

그래프경로와 같이 세팅을 해줌.

graph 함수로 각 start노드 값들을 graph의 인덱스로 주어 start노드들이 갈 수 있는 값 end를 graph 리스트의 내부 리스트로 주었다.



to_visit 이라는 스택 첫값을 0으로 주고 방문했는지 여부를 visited로 n+1값만큼(바로바로 숫자값을 인덱스와 매칭시키기 위해서) 주고 False로 2차원 리스트를 만든다.



 to_visit  스택에서 한개씩 pop 하면서 그 값을 현재값으로 하고 graph의 현재인덱스에 해당되는 인덱스가 현재값이 갈 수 있는 노드들이기 때문에 그 노드들을 다시 to_visit 스택에 저장한다.

저장된값들이 false면 true로 변환후 다시 스택값을 찾는다.



```python
# stack에서 pop을 하여 인접리스트에 접근한 다음 방문을 표기해주는 함수
def visiting(graph):
    # 시작점
    to_visit = [0]
    # 배열판
    visited = [False for _ in range(100)]

    # print(visited)

    # stack 값이 있는동안 돈다.
    while to_visit:
        # 현재 위치
        corrent = to_visit.pop()
        # 방문기록이 없다면 true로 변경하고 인접리스트의 해당되는 인덱스값을 stack에 append한다
        if not visited[corrent]:
            visited[corrent] = True
            to_visit += graph[corrent]

    return int(visited[99])

for _ in range(10):
    tc, n = map(int, input().split())

    graph = [[] for _ in range(100)]
    load = list(map(int, input().split()))
    start = []
    end = []
    for i in range(len(load)):
        if i%2 == 0:
            start += [load[i]]
        else:
            end += [load[i]]

    for i in range(n):
        graph[start[i]].append(end[i])

    print('#{} {}'.format(tc, visiting(graph)))
```

[0, 1, 0, 2, 1, 4, 1, 3, 4, 8, 4, 3, 2, 9, 2, 5, 5, 6, 5, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 3, 7]
[0, 0, 1, 1, 4, 4, 2, 2, 5, 5, 7, 7, 9, 9, 6, 3]
[1, 2, 4, 3, 8, 3, 9, 5, 6, 7, 99, 9, 8, 10, 10, 7]
[[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [], [], [], [], [], [], []]

인접리스트 생셩.



```python
T = 10
for tc in range(1, T+1):
 
    tc , N = map(int, input().split()) 
    lines = list(map(int, input().split()))
    newlst = []
 
    for idx in range(len(lines)):
        if idx % 2 == 0:
            small = []
            small.append(lines[idx])
            small.append(lines[idx+1])
            newlst.append(small)
 
    visited = [0] * 100 
    node = [[] for i in range(100)] 
    for item in newlst:
        node[item[0]].append(item[1]) 
 
 
    stack = []
    start = 0
    stack.append(start)
    visited[start] = 1

    while stack:
        start = stack.pop()
 
        for route in node[start]:
            if not visited[route]:
                stack.append(route)
                visited[route] = 1
 
 
    print('#{} {}'.format(tc, visited[-1]))
```

함수를 for문에 그대로 쓴 코드



```python
def dfs(num):
    global result
    if num == 99:
        result = 1
    for i in range(100):
        if result == 1: break
        if arr[num][i] == 1 and visit[i] == False:
            visit[i] = True
            dfs(i)
 
for _ in range(1, 11):
    tc, count = map(int, input().split())
    dir = list(map(int, input().split()))
    arr = [[0] * 100 for _ in range(100)]
    visit = [False for _ in range(100)]
    visit[0] = True
    idx, result = 0, 0
    while idx < count * 2:
        arr[dir[idx]][dir[idx+1]] = 1
        idx += 2
    print('#%d' % (tc), end = ' ')
    dfs(0)
    print(result if result == 1 else 0)
```

재귀사용코드



```python
def route99(graph):
    visited = [0] * 100
    to_go = [0]
 
    while to_go:
        current = to_go.pop()
        if current == 99:
            return 1
 
        if not visited[current]:
            visited[current] = 1
 
            for node in graph[current]:
                if not visited[node]:
                    to_go.append(node)
    return 0
 
T = 10
for _ in range(1, T + 1):
    tc, n = map(int, input().split())
    a, b = 0, 99
    graph = [[] for _ in range(100)]
    edge = list(map(int, input().split()))
 
    for idx in range(0, n * 2, 2):
        s, e = edge[idx], edge[idx+1]
        graph[s].append(e)
 
    print('#{} {}'.format(tc, route99(graph)))
```

위의 두 코드는 현재값이 99일때 바로 1을 반환하도록 함수를 짰다.

그럼 완전 탐색은 아님. (완전탐색하라고하면 return을 써서 멈추게 하면 안됨)





## #1234_비밀번호



4873 반복문자지우기와  거의 같다.



```python
def realnum(password):

    i = 1
    while len(password) > 1:
        if i >= len(password):
            break
        # 스택에서 추출
        current = password.pop(-i)
        # 마지막값과 같으면
        if current == password[-i]:
            # 마지막값도 추출
            password.pop(-i)
            if i > 1:
                i -= 1
        # 같지 않으면 다시 넣어주기
        else:
            if i == 1:
                password.insert(len(password), current)
            else:
                password.insert(-i+1, current)
            i += 1

    return ''.join(password)

for tc in range(1, 11):
    n, password = input().split()
	
    #리스트에 넣기 pop하고 삽입하려고 
    emp = []
    for i in password:
        emp.append(i)

    print('#{} {}'.format(tc, realnum(emp)))
```

stack을 이용해서 뺀값이 기존마지막과 같으면 같이 빼고 

아니면 다시 집어넣고 반복하기.



```python
T = 10
for tc in range(1, T + 1):
    n, password = input().split()
 
    stack = []
    idx = 0
    while idx < int(n):
        if not stack:
            stack.append(password[idx])
        else:
            if stack[-1] != password[idx]:
                stack.append(password[idx])
            else:
                stack.pop()
        idx += 1
 
    result = ''.join(stack)
 
    print('#{} {}'.format(tc, result))
```

첫 값을 스택에 집어넣고 다음 값이 스택값과 다르면 스택에 넣어주고 

같다면 스택값을 pop해주면 중복되는 값이 생길 수 없다.



```python
for t in range(1, 11):
    N, Password = map(str, input().split())
 
    Pass_list = list(Password)
 
    stack = []
    for num in Pass_list:
        if len(stack) != 0 and stack[-1] != num:
            stack.append(num)
        elif len(stack) == 0:
            stack.append(num)
        elif len(stack) != 0 and stack[-1] == num:
            stack.pop()
 
    print('#{} {}'.format(t, ''.join(stack)))
```

str 에서 리스트로 넣는게 아니라 리스트에서 리스트로 넣는 방식.

while문이 아니라 for문.



## #1223 계산기2

2.5)

stack의 push와 pop을 조건별로 해야해서 오래걸리고 하나씩 에러를 잡는게 까다로웠다..



출력값:

```python
952*1+33*7*6*9*1*7*1+86*61*1*5*2*4*7*43*8*2*6*78*4*5*3+7+2+6+5+1+7+6+73*6*2+6+62*4+22*49*3
```



수정후:

```python
952*+1+33**76**91**7+1+86*+61**15**24**7+43**82**6+78**45*+3+7+2+6+5+1+7+6+73**6+2+6+62*+4+22*+49**3
```



```python
def backsol(numbers):
	
    # 연산자를 쌓는 스택과 숫자와 연산자를 같이 넣어주는 back리스트 
    stack = []
    back = []
    for idx in range(N):
        # 만약 인덱스가 짝수라면 == 숫자라면 
        if idx%2 == 0:
            back.append(numbers[idx])
        # 연산자 일 떄
        else:
            if len(stack) == 0:
                stack.append(numbers[idx])
           # + 는 순위가 가장낮으므로 기존에 있던 값들을 다 pop 해서 back에 append해준다.
            elif numbers[idx] == '+':
                while stack:
                    back.append(stack.pop())
                # 이번 값은 스택에 저장 !!
                stack.append(numbers[idx])
            elif numbers[idx] == '*':
                if stack[-1] == '+':
                    stack.append(numbers[idx])
                # + 만나기 전까지 * 값들이 있다면 다 pop 해준다. 
                else:
                    while stack[-1] != '+':
                        back.append(stack.pop())
                    stack.append(numbers[idx])
    return ''.join(back)
    # return back

def solution(numbers):

    number = '0123456789'
    cal = []
    result = 0

    for idx in range(len(numbers)):
        if numbers[idx] in number:
            cal.append(int(numbers[idx]))
        else:
            if len(cal):
                if numbers[idx] == '*':
                    result += cal.pop(-2) * cal.pop()
                elif numbers[idx] == '+':
                    result += cal.pop(-2) + cal.pop()
            else:
                if numbers[idx] == '*':
                    cal.append(cal.pop(-2) * cal.pop())
                elif numbers[idx] == '+':
                    cal.append(cal.pop(-2) + cal.pop())
    return cal

N = int(input())
numbers = list(input())
# print(numbers)
# print(numbers[0]+numbers[2])
# print(type(numbers[0]),type(int(numbers[0])))

print(backsol(numbers))
# print(eval(backsol(numbers)))
print(solution(backsol(numbers)))
```

solution 함수에서 result 변수 만들필요없음.

while(cal) 안해도 됨.

```python
# 이 부분이 두번 나오는데
while stack[-1] != '+':
    back.append(stack.pop())
stack.append(numbers[idx])

# 이렇게 써서 에러남
while stack[-1] != '+':
    back.append(stack.pop())
	back.append(numbers[idx])
# or
while stack[-1] != '+':
    back.append(stack.pop())
back.append(numbers[idx])
```

튜터로 잘못된곳 수정함.

```python
952*+1+33*7*6*9*1*7*+1+86*+61*1*5*2*4*7*+43*8*2*6*+78*4*5*+3+7+2+6+5+1+7+6+73*6*+2+6+62*+4+22*+49*3
[28026, 36, 3]
```

거의 다왔다.

![image-20210224214327365](C:\Users\a\알고리즘\.SWEA_README\README.assets\image-20210224214327365.png)

마지막 두개  연산자가  스택에 남아있었음..



마지막 코드 추가로 연산자들 다 넣음

```python
		if idx > N-2:
            while stack:
                back.append(stack.pop())
    return ''.join(back)
```


28134

#1 [28134]
#2 [195767]
Traceback (most recent call last):
#3 [4293]
#4 [1592]
#5 [477326]
#6 [45647]
#7 [102951]
  File "C:/Users/a/알고리즘/1223_계산기2/sol1.py", line 66, in <module>
    print('#{} {}'.format(tc, solution(backsol(numbers))))
  File "C:/Users/a/알고리즘/1223_계산기2/sol1.py", line 24, in backsol
    while stack[-1] != '+':
IndexError: list index out of range



*가 나올때 전에 *은 하나만 있을텐데  괜히 while 문을 써서 에러가 났음 

```python
         # + 만나기 전까지 * 값들이 있다면 다 pop 해준다. 
        else:
            while stack[-1] != '+':
                back.append(stack.pop())
            stack.append(numbers[idx])
            
 # 한개만 스텍에서 빼주고 새로운값을 스택에 집어넣는다. (그냥 새로운값을 바로 집어넣어도 될 듯)
    			else:
                    if stack[-1] != '+':
                        back.append(stack.pop())
                    stack.append(numbers[idx])
```



길지만 완성된 코드 

```python
def backsol(numbers):

    stack = []
    back = []
    for idx in range(N):
        if idx%2 == 0:
            back.append(numbers[idx])
        else:
            if len(stack) == 0:
                stack.append(numbers[idx])
            elif numbers[idx] == '+':
                while stack:
                    back.append(stack.pop())
                stack.append(numbers[idx])
            elif numbers[idx] == '*':
                if stack[-1] == '+':
                    stack.append(numbers[idx])
                else:
                    if stack[-1] != '+':
                        back.append(stack.pop())
                    stack.append(numbers[idx])
        if idx > N-2:
            while stack:
                back.append(stack.pop())
    return ''.join(back)

def solution(numbers):

    number = '0123456789'
    cal = []

    for idx in range(len(numbers)):
        if numbers[idx] in number:
            cal.append(int(numbers[idx]))
        else:
            if len(cal) >= 3:
                if numbers[idx] == '*':
                    if numbers[idx] == '*':
                        cal.append(cal.pop(-2) * cal.pop())
                    elif numbers[idx] == '+':
                        cal.append(cal.pop(-2) + cal.pop())
            else:
                if numbers[idx] == '*':
                    cal.append(cal.pop(-2) * cal.pop())
                elif numbers[idx] == '+':
                    cal.append(cal.pop(-2) + cal.pop())
    return cal

for tc in range(1, 11):
    N = int(input())
    numbers = list(input())
    # print(eval(backsol(numbers)))
    print('#{} {}'.format(tc, *solution(backsol(numbers))))
```



좀 더 간단한 코드 구현 1.

```python
T = 10
for tc in range(1, T + 1):
    n = int(input())
    origin = input()
    stack = []
     
    # 1. 후위 계산식으로 변환
    back = ''
    op = {'+': 1, '*': 2}
    for idx in range(n):
        if origin[idx].isdigit():
            back += origin[idx]
        else:
            if not stack:
                stack.append(origin[idx])
            else:
                while stack and op[stack[-1]] > op[origin[idx]]:
                    back += stack.pop()
                stack.append(origin[idx])
    while stack:
        back += stack.pop()
 
    # 2. 후위 계산식 계산
    for char in back:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            y = stack.pop()
            x = stack.pop()
            stack.append(x+y)
        elif char == '*':
            y = stack.pop()
            x = stack.pop()
            stack.append(x*y)
 
    print('#{} {}'.format(tc, stack[0]))
```



이렇게 변형가능.

```python
def backsol(numbers):

    stack = []
    back = []
    for idx in range(N):
        if idx%2 == 0:
            back.append(numbers[idx])
        else:
            if len(stack) == 0:
                stack.append(numbers[idx])
            elif numbers[idx] == '+':
                while stack:
                    back.append(stack.pop())
                stack.append(numbers[idx])
            elif numbers[idx] == '*':
                if stack[-1] == '+':
                    stack.append(numbers[idx])
                else:
                    if stack[-1] != '+':
                        back.append(stack.pop())
                    stack.append(numbers[idx])
        if idx > N-2:
            while stack:
                back.append(stack.pop())
    return ''.join(back)

def solution(back):
    stack = []
    for char in back:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            y = stack.pop()
            x = stack.pop()
            stack.append(x + y)
        elif char == '*':
            y = stack.pop()
            x = stack.pop()
            stack.append(x * y)

    return stack

for tc in range(1, 11):
    N = int(input())
    numbers = list(input())
    # print(backsol(numbers))
    print('#{} {}'.format
```



숏코딩.

```python
for tc in range(1, 11):
    cnt = int(input())
    arr = input()
    stack = []
    idx, result = 0, 0
    while idx < cnt:
        if arr[idx] == '*':
            idx += 1
            stack.append(stack.pop() * int(arr[idx]))
        elif arr[idx] == '+':
            pass
        else:
            stack.append(int(arr[idx]))
        idx += 1
    while stack:
        result += stack.pop()
    print('#%d %d' % (tc, result))
```

![image-20210224222922314](C:\Users\a\알고리즘\.SWEA_README\README.assets\image-20210224222922314.png)

일단 곱셈만하고 나머지는 한번에 결과에 더해준다..



후위표기연산식을 만들어주는 사이트

https://www.mathblog.dk/tools/infix-postfix-converter/



## #4408_자기방으로들어가기

2.5) :sweat: 

​			start end

학생 a   10 100

학생 b   20  80 

이라 하였을 때, end가 작은값의 학생의 end가 

end가 큰 학생의 start보다 크다면 구간이 겹치게 된다.

시작을 cnt = 1 로 두고 풀어보자.

```python
students = []
for idx in range(N):
    # start, end = map(int, input().split())
    students.append(list(map(int, input().split())))
print(students)
```

[[10, 20], [30, 40], [50, 60], [70, 80]]

학생들 정보 받기.



```python
def q_sort(nums):
    if len(nums) <= 1:
        return nums

    left, right = [], []
    pibut = nums[0]

    # 1부터 시작해야 한다!
    for i in range(1, len(nums)):
        if nums[i] < pibut:
            left.append(nums[i])
        else:
            right.append(nums[i])

    sorted_left = q_sort(left)
    sorted_right = q_sort(right)

    return [*sorted_left, pibut, *sorted_right]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    students = []

    for idx in range(N):
        # start, end = map(int, input().split())
        students.append(list(map(int, input().split())))
    # print(students)

    # print(q_sort(students))
    for i in range(N):
        for j in range(i+1, N):
            # if students[i][1] < students[j][1] and students[i][1] > students[j][0]:
            if students[i][1] > students[j][0]:
                cnt += 1
    if cnt > 2:
        cnt -= 1
    print('#{} {}'.format(tc, cnt))
```

10개중 1개 맞았습니다.



빈리스트에 지나가는 범위마다 1을 더해주고 가장 큰 값을 구하면 되지않을까?



```python
def q_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right = [], []
    pibut = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < pibut:
            left.append(nums[i])
        else:
            right.append(nums[i])
    sorted_left = q_sort(left)
    sorted_right = q_sort(right)
    return [*sorted_left, pibut, *sorted_right]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    students = []
    cnt_list = [0]*400

    for idx in range(N):
        students.append(list(map(int, input().split())))

    students = q_sort(students)

    for i in range(N):
        for j in range(students[i][0], students[i][1]):
            cnt_list[j] += 1

    print('#{} {}'.format(tc, q_sort(cnt_list)[-1]))

```

10개 중 2개 맞았습니다.



```python
    for i in range(N):
        if students[i][1] > students[i][0]:
            for j in range(students[i][0], students[i][1]+1):
                cnt_list[j] += 1
        else:
            for j in range(students[i][0], students[i][1]-1,-1):
                cnt_list[j] += 1
```

튜터 로 확인해본 결과 1 10 2 8 같은 경우는 잘 더해주지만 range가 7 3 과 같이 거꾸로 가는경우는 더해주지 않았었다.

6개맞고 런타임에러..

마주보는 방과방 사이 통로에 번호를 붙이고, 그 번호를 지나가는 사람을 세는 방식으로 생각해보세요...?

![image-20210225110649729](C:\Users\a\알고리즘\.SWEA_README\README.assets\image-20210225110649729.png)

1-3 5-4 의 경우 통로를 공유한다..



```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = []
    # 통로의 길이 (1,2) (3,4)
    corridor = [0] * 201

    for idx in range(N):
        students.append(list(map(int, input().split())))

    # print(students)

    for i in range(N):
        if students[i][1] > students[1][0]:
            for j in range((students[i][0]+1)//2, (students[i][1]+1)//2 + 1):
                corridor[j] += 1
        else:
            for j in range((students[i][1]+1)//2, (students[i][0]+1)//2-1, -1):
                corridor[j] += 1

    # print(corridor)
    print('#{} {}'.format(tc, max(corridor)))
```

세개 맞았다.

내림차순으로 했으면서 작은걸 앞에써줌.. 4개로 변경됨



```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = []
    # 통로의 길이 (1,2) (3,4)
    corridor = [0] * 201

    for idx in range(N):
        students.append(list(map(int, input().split())))

    # print(students)

    for i in range(N):

        if students[i][0] > students[i][1]:
            for j in range((students[i][0]+1)//2, ((students[i][1]+1)//2)-1, -1):
                corridor[j] += 1
        else:
            for j in range((students[i][0]+1)//2, (students[i][1]+1)//2 + 1):
                corridor[j] += 1

    # print(corridor)
    print('#{} {}'.format(tc, max(corridor)))
```

if 와 else 순서 변경하고 성공했다..

일반적인 경우를 else 에 넣고 특수한 경우를 if에 넣으면 좋을것 같다.



다른 답코드)

```python
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 1. 방이 총 400개 / 구간은 200개
    corridor = [0] * 201
    for _ in range(n):
        # 2-1. 방 번호 a, b를 받고
        a, b = map(int, input().split())
        # 2-2. a, b 오름차순
        if a > b:
            a, b = b, a
        # 3. a-b 이동 구간 구하기
        start = (a + 1) // 2
        end = (b + 1) // 2
        # 4. 복도 구간에 이동 경로 추가
        for idx in range(start, end + 1):
            corridor[idx] += 1

    # 5. 겹치면 따로 가야 하니까 시간 추가
    print('#{} {}'.format(tc, max(corridor)))

    # T = int(input())
    # for tc in range(1, T + 1):
    #     N = int(input())
    #     room_num = [0] * 201
    #     start = ''
    #     end = ''
    #     for i in range(N):
    #         A, B = map(int, input().split())
    #         if A < B:
    #             start = A
    #             end = B
    #         else:
    #             start = B
    #             end = A
    #         if start % 2 == 0 and end % 2 == 1:
    #             for i in range(start // 2, end // 2 + 2):
    #                 room_num[i] += 1
    #         elif start % 2 == 0 and end % 2 == 0:
    #             for i in range(start // 2, end // 2 + 1):
    #                 room_num[i] += 1
    #         elif start % 2 == 1 and end % 2 == 1:
    #             for i in range(start // 2 + 1, end // 2 + 2):
    #                 room_num[i] += 1
    #         elif start % 2 == 1 and end % 2 == 0:
    #             for i in range(start // 2 + 1, end // 2 + 1):
    #                 room_num[i] += 1
    #
    #     print('#{} {}'.format(tc, max(room_num)))
```

미리 a와 b가 오름차순이 아니면 바꿔놓는것도 sort도 안써도 되고 if else로 나눌 필요가 없어져 깔끔한것 같다.



## #1860_진기의최고급붕어빵

0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 `기다리는 시간없이` 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.



n m k 공백 단위로 주어짐

a b  ...n개 n명의 사람들이 도착하는지 나타내는 시간.

```python
T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int,input().split())
    # print(n)
    people = list(map(int, input().split()))

    result = ''

    for i in range(len(people)):
        if people[i] < m:
            result = 'Possible'
        else:
            result = 'Impossible'

    print('#{} {}'.format(tc, result))
```

이렇게 하면 1000개중 383개 맞는다

```python
def q_sort(nums):
    if len(nums) <= 1:
        return nums

    left, right = [], []
    pibut = nums[0]

    # 1부터 시작해야 한다!
    for i in range(1, len(nums)):
        if nums[i] < pibut:
            left.append(nums[i])
        else:
            right.append(nums[i])

    sorted_left = q_sort(left)
    sorted_right = q_sort(right)

    return [*sorted_left, pibut, *sorted_right]


T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int,input().split())
    # print(n)
    people = list(map(int, input().split()))

    result = ''

    fish = q_sort(people)[-1] // m * k

    if n > fish:
        result = 'Impossible'
    else:
        result = 'Possible'

    print('#{} {}'.format(tc, result))
```

528개 맞았다.



```python
def fishcake(m, k, people):
    # people = q_sort(people)
    n = len(people)
    i = 0
    fish = 0
    result = 1
    latest = 0
	
    # 모든 손님이 올 때까지 
    while n > 0:
        # 붕어빵은 
        fish += ((people[i] - latest)// m) * k
        latest = (people[i]//m) * m
        if fish > 0:
            fish -= 1
            n -= 1
            i += 1
        else:
            result = 0
            break
    #     if n > 0:
    #         continue
        if n == 0 and fish > 0:
            result = 1
            break
    #         break
    #     if fish <= 0:
    #         result = 0
    if result:
        return 'Possible'
    else:
        return 'Impossible'

```

remainder의 계산이 잘못되어서 995개만 맞다가 10번만에 성공하였다.



나의 오답

```python
def fishcake(m, k, people):
    people = q_sort(people)
    n = len(people)
    i = 0
    remainder = people[0] % m
    fish = people[0] // m * k

    while n > 0:
        if i == 0:
            if people[i] < m:
                return 'Impossible'
        else:
            remainder += (people[i] - people[i - 1])
            if remainder >= m:
                fish += remainder//m * k
                remainder = remainder % m
        fish -= 1
        n -= 1
        i += 1
        if n == 0 and fish > 0:
            return 'Possible'
        if fish <= 0:
            return 'Impossible'
```



```python
def solution(n, m, k, order):
    order.sort()
    for idx in range(n):
        food = (order[idx] // m) * k
        sold = idx
        if food - (sold+1) < 0:
            return 'Impossible'
    return 'Possible'
 
T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    order = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(n, m, k, order)))
```

이렇게 붕어빵을 idx가 오는 개수 +1 만큼 주는거니까 이렇게 짧게 표현도 가능하다..



```python
T = int(input())
 
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
 
    max_time = 0
    for customer in customers:
        if customer > max_time:
            max_time = customer
 
    bread = -K
    for i in range(max_time + 1):
        if not i % M:
            bread += K
        if i in customers:
            bread -= customers.count(i)
            if bread < 0:
                result = 'Impossible'
                break
    else:
        result = 'Possible'
 
    print('#{} {}'.format(tc, result))

```

다른 답



[379, 577, 1215, 1244, 1411, 1506, 1702, 1708, 1758, 2059]
19
#369 Possible
[94, 94, 94, 94, 94, 94, 94, 94, 94, 94]
95
#370 Impossible



##### tc의 sorting된값들을 작은값부터보면 결국 m보다 작은값이 없으면 답은 'Possible'이었다.





## #4615_재미있는 오셀로 게임



진짜 재미없다..

```python
#  # 위 아래
    if oslo[0] == 1 and board[n][oslo[1]] == oslo[-1]:
        inner = []
        for r in range(2, n):
            inner.append(board[r][oslo[1]])
        if oslo[-1] not in inner:

            for i in range(1, 1 + n):
                board[i][oslo[1]] = oslo[-1]
        elif oslo[0] == n and board[1][oslo[1]] == oslo[-1]:
            for i in range(1, 1 + n):
                board[i][oslo[1]] = oslo[-1]

    ## 대각선
    if oslo[0:2] == [1, 1] and board[n][n] == oslo[-1]:
        inner = []
        for r in range(2, n):
            inner.append( board[r][r])
        if oslo[-1] not in inner:
                
            for i in range(1, 1 + n):
                for j in range(1, 1 + n):
                    if i == j:
                        board[i][j] = oslo[-1]
    
        elif oslo[0:2] == [n, n] and board[1][1] == oslo[-1]:
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i == j:
                        board[i][j] = oslo[-1]

    # 역 대각선
    if oslo[0:2] == [1, n] and board[n][1] == oslo[-1]:
        
        inner = []
        for r in range(2, n):
            for r2 in range(2, n):
                if r + r2 == n + 1
                    inner.append(board[r][r2])
                if oslo[-1] not in inner:
                        
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if i + j == n + 1:
                                board[i][j] = oslo[-1]
            
                elif oslo[0:2] == [n, n] and board[1][1] == oslo[-1]:
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if i + j == n + 1:
                                board[i][j] = oslo[-1]

    # 양 옆
    if oslo[1] == 1 and board[oslo[0]][n] == oslo[-1]:
        inner = []
        for r in range(2, n):
            inner.append(board[oslo[0]][r])
        if oslo[-1] not in inner:
                
            for i in range(1, 1 + n):
                board[oslo[0]][i] = oslo[-1]
        elif oslo[1] == n and board[oslo[0]][1] == oslo[-1]:
            for i in range(1, 1 + n):
                board[oslo[0]][i] = oslo[-1]
```



##### 상하좌우 4방향이 아니라 8방향을 보고 바로 옆에 자신과 다른돌 그리고 한칸 더 같은 방향으로 가면 자신과 같은 돌이 있어야 한다.



delta 이동 복습

```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    matrix.append([0] * (N+2))
    print(matrix)
    for _ in range(N):
        matrix.append(
           [0, *map(int, input().split()), 0]
        )
    print(matrix)
    matrix.append([0] * (N + 2))
    print(matrix)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    total = 0

    # 가장자리 미포함
    for y in range(1, N+1):  # 1, 2, 3, 4, 5 ... N
        for x in range(1, N+1):
            abs_sum = 0
            for d in range(4):
                center = matrix[y][x]
                test_y = y + dy[d]
                test_x = x + dx[d]
                around = matrix[test_y][test_x]
                if around:
                    abs_sum += abs(center - around)
            total += abs_sum

    print("#{} {}".format(tc, total))
```

상하좌우로 0을 덮고 계산 



[[0, 0, 0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 0], [0, 4, 5, 6, 0], [0, 7, 8, 9, 0]]
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 0], [0, 4, 5, 6, 0], [0, 7, 8, 9, 0], [0, 0, 0, 0, 0]]

#1 48



[[0, 0, 0, 0, 0, 0, 0]]
[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 0], [0, 6, 7, 8, 9, 10, 0], [0, 11, 12, 13, 14, 15, 0], [0, 16, 17, 18, 19, 20, 0], [0, 21, 22, 23, 24, 25, 0]]
[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 0], [0, 6, 7, 8, 9, 10, 0], [0, 11, 12, 13, 14, 15, 0], [0, 16, 17, 18, 19, 20, 0], [0, 21, 22, 23, 24, 25, 0], [0, 0, 0, 0, 0, 0, 0]]
#2 240



```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(matrix)
    #  상하 좌우
    dc = [-1, 1, 0, 0] #dy
    dr = [0, 0, -1, 1] #dx
    total = 0

    # 가장자리 미포함
    for y in range(N):
        for x in range(N):
            abs_sum = 0
            for d in range(4):
                center = matrix[y][x]
                test_y = y + dc[d]
                test_x = x + dr[d]
                # 가장자리가 포함될 수 없음
                if 0 <= test_x < N and 0 <= test_y < N:
                    around = matrix[test_y][test_x]
                    abs_sum += abs(center - around)
            total += abs_sum

    print("#{} {}".format(tc, total))
```

양옆에 0으로 덮지 않고 if조건문으로 제어 



```python
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())



    board = [[0]*(n+2) for _ in range(n+2)]

    cen1, cen2 = int(n/2), int(n/2)+1

    for i in range(cen1,cen2+1):
        for j in range(cen1,cen2+1):
            if i == j:
                board[i][j] += 2
            else:
                board[i][j] += 1
    # print(board)

    dc = [-1, 0, 1]
    dr = [-1, 0, 1]

    # 들어오는 돌의 위치
    for _ in range(m):
        othello = list(map(int, input().split()))

        if othello[-1] == 1:
            board[othello[0]][othello[1]] = 1
        elif othello[-1] == 2:
            board[othello[0]][othello[1]] = 2

        # 사이에 낀 돌을 바꾸기.
        for i in range(len(board)):
            for j in range(len(board[0])):
                for c in range(3):
                    for r in range(3):

                        # 사이에 낀 돌을 바꾸기.
                        center = board[i][j]
                        test_c = i + dc[c]
                        test_r = j + dr[r]
                        test_cc = test_c + dc[c]
                        test_rr = test_r + dr[r]

                        if center == 1 and board[test_c][test_r] == 2:
                            if board[test_cc][test_rr] == center:
                                board[test_c][test_r] = center
                        elif center == 2 and board[test_c][test_r] == 1:
                            if board[test_cc][test_rr] == center:
                                board[test_c][test_r] = center
    cnt1 = 0
    cnt2 = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1



    print('#{} {} {}'.format(tc, cnt1, cnt2))
```

30 개중 2개맞은 code..

8방향을 살피며 사이에 있는 돌만 같은 돌로 처리해주었지 한개의 돌 이상을 사이에 두고 있는 경우를 처리해주지 못하였다.

