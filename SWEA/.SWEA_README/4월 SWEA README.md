[TOC]

# 4월 SWEA README

 :smiley:  :slightly_smiling_face:  :sweat:  :face_with_head_bandage:

4월 알고리즘도 화이팅

1일 1 commit 🤸‍♀️



## #1231_중위순회

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE&problemTitle=1231&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

:sweat:

![image-20210405233736348](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210405233736348.png)

![image-20210405233753122](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210405233753122.png)



이진트리의 순회(트리의 노드들을 체계적으로 방문하는 것) 의 세가지 방법중 중위 순회에 관한 문제이다.



- 전위 순회: VLR

  부모노드 방문 후 자식노드를 좌우 순서로 방문

- 중위 순회: LVR

  왼쪽 자식노드 부모노드 오른쪽 노드 순으로 방문

- 후위 순회: LRV

  자식노드를 좌우 순서로 방문 후 부모노드로 방문



```python
## 중위순회 LVR 레프트 -> 루트 -> 라이트
def inorder(n):
    if int(n) > 0:
        # 왼쪽부터 방문
        inorder(left[int(n)])
        # 더 이상 방문할 왼쪽이 없다면 그 노드를 출력
        print(word[int(n)], end=' ')
        # 출력후 오른쪽 자식노드 방문 
        inorder(right[int(n)])

T = 10 
for tc in range(T):
    V = int(input())
    left = [0]*(V+1)
    right = [0]*(V+1)
    word = [0]*(V+1)

    for i in range(V):
        N = list(input().split())
        # print(N)
        # 단어 그래프를 만들어줌
        word[int(N[0])] = N[1]
        if len(N) == 4:
            # 네번째 값까지 있다면 양쪽에 넣어줌
            left[int(N[0])] = N[2]
            right[int(N[0])] = N[3]
        if len(N) == 3:
            # 길이가 3이라면 왼쪽에 넣어줌
            left[int(N[0])] = N[2]
          
    print('#{}'.format(tc+1), end=' ')
    inorder(1)
    print()
```



방문 순서만 바꿔주면 전위순회와 후위순회 가능.

```python
 ## 전위순회 VLR 루트 -> 레프트 -> 라이트
 def preorder(n):
     if int(n) > 0:
         print(word[int(n)], end=' ')
         preorder(left[int(n)])
         preorder(right[int(n)])

        
## 후위순회 LRV 레프트 -> 라이트 -> 루트
def postorder(n):
    if int(n) > 0:
        postorder(left[int(n)])
        postorder(right[int(n)])
        print(word[int(n)], end=' ')
```



인풋값을 리스트로 받아 문자열을 숫자열로 그때그때 바꿔주고 그래프에 해당 트리를

이차원 배열로 만들어 방문해주는 형식으로 접근하였다.



다른 풀이

```python
## 여러번 말고 한번에 받아서 2차원 리스트로 만들어주는 방법
for tc in range(1, 2):
    n = int(input())

    node = [[0]] + [list(map(str, input().split())) for _ in range(n)]
    print(node)

# 반복문을 통한 값 삽입 & 왼쪽 오른쪽을 만들지 않고 트리의 배수관계를 이용해서 함수를 정의
T = 10

def inorder(cnt):
    global result
 
    if cnt <= N:
        inorder(cnt * 2)
        result += str(word[cnt])
        inorder(cnt * 2 + 1)
 
 
for tc in range(1, T+1):
    N = int(input())
    node = [0] * (N + 1)
    for n in range(1, N + 1):
        node[n] = input().split()[1:]
    # print(node)
 
    word = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        word[i] = node[i][0]
    result = ''
    inorder(1)
    print('#{} {}'.format(tc, result))
    
    
### 위와 비슷
# 그래프를 사용하지않고? 인덱스와 알파벳만 저장
def inorder(n):
    if n < V+1:
        inorder(n*2)
        print(node[n], end='')
        inorder(n*2+1)
 
T = 10
global V
for tc in range(1, T+1):
    answer =""
    V = int(input())
    node = [0] * (V+1)
    for i in range(1, V+1):
        values = input().split()
        index = int(values[0])
        node[index] = values[1] 
 
    print("#{}".format(tc), end=' ')
    inorder(1)
    print()
```



wfost rae

software

sotf aerw



## #5174_subtree

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg



![image-20210406143710565](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406143710565.png)



![image-20210406143735688](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406143735688.png)



```python
# 3. 해당 노드의 아래 있는 노드들을 탐색하고 그때마다 1씩 더해준다.
def order(n):
    global cnt

    if tree[0][n] != 0:
        num = tree[0][n]
        cnt += 1
        order(num)
    if tree[1][n] != 0:
        num = tree[1][n]
        cnt += 1
        order(num)
    return cnt


T = int(input())
for tc in range(1, T + 1):
    n, num = map(int, input().split())
    node = list(map(int, input().split()))
    # print(node)
    # print(max(node))
    tree = [[0] * (n + 2) for _ in range(2)]
    # print(tree)

    # 1. 2개마다 앞에 값을 인덱스 뒤에값을 해당 인덱스 위치의 값으로 넣는다
    for i in range(n * 2):
        if i % 2 == 0:
            n1, n2 = node[i], node[i + 1]
            # 2-1. 왼쪽 자식이 없으면 왼쪽부터
            if tree[0][n1] == 0:
                tree[0][n1] = n2
            # 2-2. 있으면 오른쪽도
            else:
                tree[1][n1] = n2
	# 생성된 트리 확인 
    # print(tree)
    cnt = 1
    print('#{} {}'.format(tc, order(num)))

```



2차원 행렬로 빈 트리를 만들어주고 

앞에 있는 값들을 인덱스로 뒤에 값들을 집어넣어 이차원 리스트를 만들어주었다.

그리고 숫자가 들어갔을때 해당 숫자의 아래있는 자식노드들을 재귀로 찾아가면서  cnt 를 하나씩 늘렸다.





## #5176_이진탐색

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

![image-20210406144830000](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406144830000.png)

![image-20210406144844913](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406144844913.png)



숫자하나가 주어지는데 그거가지고 어떻게 트리를 만들지 몰라서 고민을 많이했다.



```python
# 완전이진트리 만들기
def bintree(n):
    global cnt
    # 범위 이내라면 시도 (4*2 4*2+1 5*2..등등 리프노드에서 더이상 뻗을 수 없음)
    if n <= N:
        # 왼쪽 자식으로 감
        bintree(n*2)
        # 더 이상 왼쪽으로 못가면 값을 1부터 집어넣는다
        tree[n] = cnt
        cnt += 1
        # 노드에 값을 넣으면 오른쪽으로 자식으로 이동
        bintree(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # print(N) # 6

    tree = [0 for _ in range(N+1)]
    # print(tree) % [0]*7
    cnt = 1
    # 루트 1부터 시작해서 완전이진트리 만들기
    bintree(1)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')

```



중위순회로 빈 트리에 값을 집어넣으면  왼쪽값이 가장 작은 값이고 

그리고 루트 그리고 오른쪽 자식으로 가면서 왼쪽값이 가장작고 오른쪽값이 가장 커지게 된다.

더 이상 왼쪽 자식으로 가지못한다면 cnt 1부터 대입해주는 방식.





## #5177_이진힙



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg



![image-20210406145336028](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406145336028.png)

![image-20210406150321369](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406150321369.png)



전위순회는 						중위순회는		후위순회는

​		1										  4						   6

​	2     5								  2	   6				  3	   5

3  4    6								1 3    5 				1  2   4

부모노드 < 자식노드		 L < V < R     		부모노드 > 자식노드 





최소힙은 부모노드가 작아야함.

전위순회형식



```python
# 부모노드가 자식노드보다 클 때 두 노드의 위치를 바꾸기
def change(n):
    if node[n] < node[n//2]:
        node[n//2], node[n] = node[n], node[n//2]
        # 이 코드를 넣지 않으면 tc 3개만 통과 (다시 한번 조상노드와 비교해서 조상노드보다 값이 작은지 확인)
        change(n//2)

# 조상노드들의 값을 모두 더해주기
def solve(n):
    cnt = 0
    while n > 0:
        cnt += node[n//2]
        # 조상노드로 또 가기
        n //= 2
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = list(map(int, input().split()))
    # 첫번째 인덱스에 0 추가
    node.insert(0, 0)
    # print(node)

    # 인덱스 1일때는 0과 바꾸면 안되므로 높이 2에서부터 change함수 시작
    for i in range(len(node)):
       if i >= 2:
           change(i)

    # print(node)
    # 결과값 출력 
    print(f'#{tc} {solve(N)}')
```



```python
# 자식노드와 부모노드는 n//2 와 n*2, n*2+1 관계로 되어있다는 것을 이용하여야 한다.
```





## #5178_노드의 합



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

![image-20210406211003528](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406211003528.png)

![image-20210406211145130](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406211145130.png)



```python
def add(n):
    if n > 1:
        node[n//2] += node[n]
        # 4. 이미 왼쪽 자식에게 더해진 조상노드는 오른쪽 자식노드에게 더해지고나면 
        # 그 위 조상노드에 더한값 반영하기
        if node[n//2] != node[n]:
            add(n//2)
        # 5. 마지막 노드가 외자식이라면 얘는 바로 더해준다.
        elif n == N:
            add(n//2)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 1. 빈 노드 값 리스트 만들기
    node = [0 for _ in range(N+1)]
    # 2. 리프 노드들 값을 각 자리에 넣어주기
    for i in range(M):
        n1, n2 = map(int, input().split())
        node[n1] = n2
        # 3. 부모노드들에게 자식노드의 값을 더해주는 함수
        add(n1)
    # print(node)
    print(f'#{tc} {node[L]}')

```



포인트는 add함수를 통해 자식노드들을 부모노드로 더 해줄 때

- 더해주고 바로 재귀로 들어가면 안된다. (중첩이 됨)

- 왼쪽 노드 더해주고 오른쪽 노드 더 할 때만 부모노드로 반영하면 안되고

  마지막 노드가 하나일 때도 재귀를 하게 해줘야 함.

  

아직은 처음에 트리를 손으로는 그릴 수 있는데 어떻게 로직을 짜야할 지 고민하는데 시간이 오래걸린다..





## #1232_사칙연산



https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD&categoryId=AV141J8KAIcCFAYD&categoryType=CODE&problemTitle=1232&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&



![image-20210406212421900](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406212421900.png)

![image-20210406212436689](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210406212436689.png)



높이를 고려해주지 않으면  tc 1번 빼고 오답이 나온다.

중위순회로 하는게 아니라 후위순회로 하고 그 리스트를 스택으로 해결해야 한다.



```python
import sys
sys.stdin = open('input.txt')


# 4. 연산자를 계산해주는 함수
def sol(x):
    n1, n2 = ans.pop(-2), ans.pop()
    if x == '+':
        n = n1 + n2
    elif x == '-':
        n = n1 - n2
    elif x == '*':
        n = n1 * n2
    else:
        n = n1 / n2
    # 4-1. 계산후 다시 스택에 삽입
    ans.append(n)

# 3. 후위연산을 위한 함수
def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        # 3-1. 숫자형이면 바로 스택에 삽입
        if type(node[n]) == int:
            ans.append(node[n])
        # 3-2. 연산자 계산해주는 함수로 이동
        else:
            sol(node[n])

# 0.
T = 10
for tc in range(1, 11):
    N = int(input())
    node = [0 for _ in range(N+1)]
    left = [0 for _ in range(N+1)]
    right = [0 for _ in range(N+1)]
    ans = []
    for i in range(N):
        nod = list(input().split())
        # 1. 연산자와 자식노드들이 있는 경우
        if len(nod) == 4:
            n1 = int(nod[0])
            n2 = nod[1]
            n3 = int(nod[2])
            n4 = int(nod[3])
            left[n1] = n3
            right[n1] = n4
        # 2. 숫자만있는 노드
        elif len(nod) == 2:
            n1 = int(nod[0])
            n2 = int(nod[1])
        node[n1] = n2
    # 3. 후위연산을 위한 함수 실행
    postorder(1)
    # 5. 대괄호 제거
    ans = int(ans[0])

    print(f'#{tc} {ans}')
```



숫자형이 아닐때만 연산을 해준다. 스택을 사용하여야 한다. 



중위순회로 일렬로 나열한 다음에 계산하려고 하였는데 그렇게 되면 높이를 고려해주지 못해서 해결하기 어려웠다.

그래서 후위순회로 리프 노드들부터 조상노드로 올라가면서 스택을 활용하여 계산해주면 되었다.







## #1248_공통조상

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE&problemTitle=1248&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



![image-20210408172855204](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210408172855204.png)

![image-20210408172949902](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210408172949902.png)





```python
# 5. 서브 트리의 크기를 구하는 함수
def count(n):
    global cnt
    cnt += 1
    # 자식노드의 값이 있다면 재귀를 통해서 서브트리 카운트
    if tree[n][0]:
        for child in tree[n]:
            count(child)

    # 아래 코드는 재귀에러 발생
    # for i in tree[n]:
    #     # 자식노드의 개수만큼 카운팅해준다.
    #     cnt += 1
    #     cnt_list.append(i)
    # # 카운트 리스트에 자식 노드들을 넣어주고 하나씩 빼면서 그 노드의 자식노드들을 append 한다.
    # while cnt_list:
    #     n = cnt_list.pop()
    #     # 자식노드에 연결된 노드들이 없다면 종료한다.
    #     if tree[n][0]:
    #         count(n)
    return cnt


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    # 0 두개로 채워주는 트리
    tree = [[0 for _ in range(2)] for _ in range(V+1)]
    node = list(map(int, input().split()))

    # 1. 트리가 비어있으면 부모 자식 정점을 이어주고 있다면 값을 추가해줌
    for i in range(E*2):
        if i%2 == 0:
            if tree[node[i]] == [0, 0]:
                tree[node[i]] = [node[i+1]]
            else:
                tree[node[i]] += [node[i+1]]

    # 2-1. 빈 리스트에 첫번째 정점의 조상들을 넣어준다.
    anc_node1 = []
    while True:
        for i in range(len(tree)):
            if n1 in tree[i]:
                anc_node1 += [i]
                n1 = i
        if n1 == 1:
            break
    # print(anc_node1) # [5, 3, 1]

    # 2-2. 빈 리스트에 두번째 정점의 조상들을 넣어준다.
    anc_node2 = []
    while True:
        for i in range(len(tree)):
            if n2 in tree[i]:
                anc_node2 += [i]
                n2 = i
        if n2 == 1:
            break
    # print(anc_node2) # [11, 6, 3, 1]


    # 3. 두 정점의 공통조상을 찾아준다.
    same_anc = []
    if len(anc_node1) >= len(anc_node2):
        for i in anc_node2:
            if i in anc_node1:
                same_anc.append(i)
    else:
        for i in anc_node1:
            if i in anc_node2:
                same_anc.append(i)

    cnt_list = []
    # 처음으로 만나는 공통조상은 가장 앞의 값이다.
    n = same_anc[0]
    cnt = 0
    # 4. 가장 앞에 있는 공통조상의 서브트리의 크기를 구하는 함수를 실행한다.
    total = count(same_anc[0])

    # 6. 결과값을 출력한다.
    print(f'#{tc} {same_anc[0]} {total}')

```





왼쪽오른쪽 자식노드로 나눠서 만드는 트리

```python
   # 2 1 2 5 1 6 5 3 6 4 # 노드 연결
    tree = [[0] * (n + 2) for _ in range(2)]
    # print(tree)

    # 1. 2개마다 앞에 값을 인덱스 뒤에값을 해당 인덱스 위치의 값으로 넣는다
    for i in range(n * 2):
        if i % 2 == 0:
            n1, n2 = node[i], node[i + 1]
            # 2-1. 왼쪽 자식이 없으면 왼쪽부터
            if tree[0][n1] == 0:
                tree[0][n1] = n2
            # 2-2. 있으면 오른쪽도
            else:
                tree[1][n1] = n2

    # print(tree)
#[[0, 6, 1, 0, 0, 3, 4], [0, 0, 5, 0, 0, 0, 0]]

#[[0, 0, 6, 0, 1, 3, 4], [0, 0, 0, 0, 0, 0, 5]]
```

처럼 만들거나 



있는 값만 넣는 방식인

```python
    # 2-1. 부모 인덱스를 기준으로 자식 기록 tree
    tree = [[] for _ in range(v+1)]
    # 2-2. 자식 인덱스를 기준으로 부모 기록 tree
    baby_tree = [0] * (v+1)

    for i in range(e):
        n1, n2 = edges[2*i], edges[2*i+1]
        tree[n1].append(n2)
        baby_tree[n2] = n1
    # [[], [2, 3], [4], [5, 6], [7], [9, 8], [11, 10], [12], [], [], [], [13], [], []]
```

트리를 생성하지 않고



0값을 두개씩 만든 2차원 리스트에 값이 있을 때만 넣는 식으로 

[[0, 0], [2, 3], [4], [5, 6], [7], [9, 8], [11, 10], [12], [0, 0], [0, 0], [0, 0], [13], [0, 0], [0, 0]]

트리를 생성하였다.



공통조상은 바로 찾아서 추출해주고 공통조상의 subtree의 개수를 계산할 때 함수를 정의하여서 사용하였다.

처음에는 빈 리스트에 넣고 pop() 해주는 방식으로 재귀에러가 나서 헤매었으나 

빈값이 아니라면 그 자식들을 바로 카운트 함수에 넣어주는 재귀방식으로 해결하였다.



`※ 에러명: RecursionError: maximum recursion depth exceeded` 

>  기존 재귀식의 호출횟수에는 문제가 없었던거 처럼 보이나, 함수내에서 append와 pop을 하면서 스택이 쌓여 파이썬 인터프리터 상에서 재귀 맥시멈값인 1000을 돌파하여 에러가 발생하였다.



코드를 공유하면서 사람들이 코드를 알아볼 수 있을까 걱정이 되었다.

알고리즘 구현 능력이 향상된다면 사람들이 알아보기 쉽고 간편한 코드를 만들어야겠다. 

(누가봐도 알기 쉬운 변수명, 불필요한 스탭 생략.. 등)





## #5215_햄버거 다이어트



[swea 문제링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT)



![image-20210410203727671](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210410203727671.png)

![image-20210410204844180](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210410204844180.png)



```python
def find_max(idx, score, k):
    global max_score

    if k > L:
        return
    if score >= max_score:
        max_score = score

    if idx == N:
        return
    
    # 첫번째 재귀문이 잘못됨
    find_max(idx+1, burger[idx][0], burger[idx][1])
    find_max(idx+1, score + burger[idx][0], k+burger[idx][1])


T = int(input())
N, L = map(int, input().split())
burger = []
for _ in range(N):
    t, k = map(int, input().split())
    burger.append([t, k])
print(burger)
max_score = 0
find_max(0, 0, 0)
print(max_score)
```



이렇게 작성한다면 각 재료 하나만 있을때와 첫번째재료부터 제한 칼로리 이전까지의 함수만 호출되고 1번없고 2번있고 3번없고 이런식의 조합이 불가능하다.



그래서 해당 재료를 포함시키지 않는 재귀함수를 아래와 같이 만들어주어야 한다.

```python
def find_max(idx, score, k):
    global max_score

    # 제한 칼로리를 넘어서면 멈춘다
    if k > L:
        return
    # 점수가 기존값보다 커지면 최대점수로 바꾼다
    if score >= max_score:
        max_score = score

    # 정해놓은 재료만큼 오면 멈춤다
    if idx == N:
        return

    # 해당재료를 포함시키지 않을 때
    find_max(idx+1, score, k)
    # 해당재료를 포함시켜줄 때
    find_max(idx+1, score + burger[idx][0], k+burger[idx][1])


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    burger = []
    for _ in range(N):
        t, k = map(int, input().split())
        burger.append([t, k])
    # print(burger)
    max_score = 0
    # 아무것도 없을 때부터 시작함 
    find_max(0, 0, 0)
    print(f'#{tc} {max_score}')
```





```python
T = int(input())
for tc in range(1, T + 1):
    n, l = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]
 
    result = 0
    # 2의 n승만큼 부분집합을 만든다
    for i in range(1 << n):
        # 칼로리와 점수는 리셋 
        t = k = 0
        for j in range(n):
            if i & (1 << j):
                t += info[j][0]
                k += info[j][1]
                # 제한칼로리보다 크면 멈춘다.
                if k > l:
                    break
 		# 제한칼로리보다 칼로리가 낮은데 점수가 기존점수보다 크면 기존점수 대체시킨다.
        if k <= l and t > result:
            result = t
 
    print('#{} {}'.format(tc, result))
```

비트연산자로 조합의 모든 부분집합의 개수를 구하는 방법.



메모리는 적게 차지하나 실행시간이 오래걸린다는 단점이 있다.





아직 조합, 재귀문, 비트연산에 대한 이해가 부족함을 느꼈다.

그리고 아직 DP에 대해서는 거의 모른다고 생각한다.

미루지 말고 DP에 대한 학습을 해야겠다...





## #1240_단순 2진 암호코드



[문제링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=1240&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

![image-20210413003159832](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413003159832.png)

![image-20210413003330081](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413003330081.png)

![image-20210413003345233](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413003345233.png)

![image-20210413003356171](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413003356171.png)



문제를 이해하는게 쉽지 않았는데, 나만 그런거 같지는 않다..



여러가지 찾아야 할 것들이 많다고 생각했다.

n개의 줄중에 암호가 있는 줄을 찾아야 했고 m개의 숫자중에 암호가 아닌 숫자를 걸러야 했다.



이 둘을 찾고나서 진짜 숫자를 찾는 암호를 풀기위해 7개씩 끊어서 숫자를 찾고

그 숫자들이 진짜 암호의 조건에 부합하는지 확인해주는 함수를 통해서 값을 산출하였다.



```python

# 3. 진짜 숫자를 찾는 함수
def my_number(n):
    for i in range(10):
        if n == number_list[i]:
            return i


# 4. 올바른 코드일 때 코드의 총합을 return 시킴
def check(n):
    odd = 0
    even = 0
    for i in range(7):
        if i%2 == 0:
            odd += n[i]
        else:
            even += n[i]
    # 10으로 나누어 떨어져야 함
    if (odd*3 + even + n[7]) % 10 == 0:
        return sum(n)
    # 코드가 아니면 0
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 0. 암호코드 정보
    hidden_code = [list(map(int, input())) for _ in range(n)]

    # 0. 숫자정보
    number_list = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1],
                   [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]

    # 1-1. 값이 들어있는 행찾기
    my_i = 0
    # 1-1. 시작할 위치를 찾기 위해 마지막 1 뒤에 0이 몇개있는지 확인하기
    emp = []
    for i in range(n):
        for j in range(m-1,-1,-1):
            if hidden_code[i][j] == 1:
                emp += [j]
                my_i = i
                break
    # 1-1. 값이 들어있는 행찾기
    # print(my_i)

    # 1-1. 버려지는 숫자들
    # print(emp)

    # 1-2. 순회를 시작할 위치
    # print(m - 56 - (m - emp[0] - 1))
    fr = m - 56 - (m - emp[0] - 1)
    # print(fr)

    # 2. 진짜 코드 찾기
    code = []
    # 8개의 숫자
    for i in range(8):
        number = []
        # 7개씩 끊어서 읽기
        for j in range(fr+i*7, fr+i*7+7):
            number.append(hidden_code[my_i][j])
        # print(number)

        # 2-1. 실제 숫자를 찾는 함수를 실행시켜서 code에 append
        code.append(my_number(number))

    # 5. 결과 값 출력
    print(f'#{tc} {check(code)}')

```





## #5185_이진수



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT

![image-20210413114017869](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413114017869.png)



변환에 있어서 숙달되지 않았다.

숫자는 join이 되지 않는다.

'3' < '4' 실수로 된 숫자끼리 비교가 가능하다.



```python
# 2. 문자라면 16진수로
def AtoH(c):
    # (9 미만으로 주어서 테케 3개만 맞음)
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

# 3. 16진수는 2진수로
def HtoD(n):
    for i in range(len(asc)):
        if n == i:
            return asc[i]


T = int(input())
for tc in range(1, T+1):
    n, m = input().split()
    # n은 숫자로 변환
    n = int(n)

    asc = [[0, 0, 0, 0],  #2진법 - 0(16진법)
           [0, 0, 0, 1],  #2진법 - 1(16진법)
           [0, 0, 1, 0],  #2진법 - 2(16진법)
           [0, 0, 1, 1],  #2진법 - 3(16진법)
           [0, 1, 0, 0],  #2진법 - 4(16진법)
           [0, 1, 0, 1],  #2진법 - 5(16진법)
           [0, 1, 1, 0],  #2진법 - 6(16진법)
           [0, 1, 1, 1],  #2진법 - 7(16진법)
           [1, 0, 0, 0],  #2진법 - 8(16진법)
           [1, 0, 0, 1],  #2진법 - 9(16진법)
           [1, 0, 1, 0],  #2진법 - A(16진법) - 10
           [1, 0, 1, 1],  #2진법 - B(16진법) - 11
           [1, 1, 0, 0],  #2진법 - C(16진법) - 12
           [1, 1, 0, 1],  #2진법 - D(16진법) - 13
           [1, 1, 1, 0],  #2진법 - E(16진법) - 14
           [1, 1, 1, 1]]  #2진법 - F(16진법) - 15

    ans = []
    # 1. 문자 -> 16진수 -> 2진수로 변환해주는 함수 2개를 통해서 빈 리스트에 extend
    for i in range(n):
        # extend 로 하면 리스트로 안 집어넣고 원소로 집어넣음
        ans.extend(HtoD(AtoH(m[i])))

    # 4. 숫자는 join이 안되므로 문자열 리스트로 변환시킨 다음에 join
    ans = ''.join(list(map(str, ans)))
    print(f'#{tc} {ans}')

```





## #5186_이진수2



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT

![image-20210413135402304](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413135402304.png)



소수를 이진표기로 어떻게 하는지 알아야 한다.

다행히 문제에 짧은 설명이 있다.

이해가 안된다면 한 번 다른 숫자를 이진표기로 해보면 좋은것 같다.

0.1로 이진 표기가 가능한 0.5는 2의 -1승이다.

만약 2를 곱해서 1이 된다면 더 이상 해줄 것이 없다.



2를 곱해서 1이 되면 이진표기를 종료하는 함수를 만든다.

만약 1을 넘는다면 1을 빼주고 다시 소수점만 함수를 돌려주고,

1이 넘지 않아도 다시 2를 곱하며 1이 되는지 봐준다.



반복하다보면 1이 넘는 순간이 오고 넘는다면 그때 해당 자리수에 1이 들어가게 된다.

ex) 0.2는 2를 세번곱해야 1이 넘는다  -> 0.001 소수점 3째 자리에 1이 찍힌다.



해당 자리수가 지날 때마다 카운팅을 해주며 만약 12가 넘어가면 'overflow'를 출력해준다.



```python
# 2. 2를 곱해가면서 1이 넘으면 해당 위치(-1승..-2승..)에 1을 집어넣는 이진표기법
def FtoB(n):
    global cnt, result
    new_n = n * 2
    # 결과값에 저장
    result += str(int(new_n))
    # 자리수를 카운팅
    cnt += 1
    # 1이 되면 끝
    if new_n == 1:
        return
    # 1이 넘으면 소수부분만 재귀로 다시 실행
    else:
        n = new_n - int(new_n)
        FtoB(n)
    # 12번째 자리를 넘으면 오버플로우 출력
    if cnt > 12:
        result = 'overflow'
        return


T = int(input())
for tc in range(1, T+1):
    # 0. 실수값을 입력받는다
    num = float(input())

    # 0. 자리수와 출력문의 초기값
    cnt = 0
    result = ''
    # 1. 이진수로 변환시키면서 자리수를 저장하면서 세어주는 함수
    FtoB(num)
    # 3. 결과값 출력
    print(f'#{tc} {result}')
```







## #10726_이진수표현

(응용)



https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS&categoryId=AXRSXf_a9qsDFAXS&categoryType=CODE&problemTitle=10726&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



![image-20210413153201956](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413153201956.png)



이번에는정수를 이진표기로 바꿔주는 함수를 만들어야 했다.

바꿔주고 나서 n개의 비트가 1로 되어있는지 확인하면 되었다.



```python
# 2. 함수 실행
def OnOff(num):
    global result
    # 값이 0이면 while 문에 안 들어가므로 바로 'OFF'
    if not num:
        return 'OFF'
    # 임시로 이진표기의 비트를 뒤에서부터 담아주는 리스트
    temp = []
    while num:
        q = num//2
        remain = num%2
        # 2로 나눈 나머지를 임시 리스트에 삽입
        temp += [remain]
        # 2이상으로 해주면 마지막 2로 나눴을 때 나머지가 안 더해짐
        if q >= 1:
            num = q
        # 처음부터 n개까지 더해보면 모두 1로 채워졌는지 알 수 있음
        else:
            if sum(temp[:n]) == n:
                return 'ON'
            else:
                return 'OFF'


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    result = []
    # 1. 숫자 m의 이진표기법 마지막 n개의 비트가 모두 켜져있는지 확인하는 함수
    ans = OnOff(m)
    # 결과값 출력
    print(f'#{tc} {ans}')
```





## #3752_가능한 시험점수

(응용)

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn



![image-20210413173836845](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413173836845.png)

![image-20210413173848933](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210413173848933.png)



햄버거 문제처럼  가능한 부분집합을 모두 구한다음 set을 이용하여 중복을 제거해주려고 했는데

runtime error가 발생하여서 실행시간과 메모리를 확인하였는데 메모리가 다른 정답자에 비해서 4배정도 높았고 실행시간은 6배 높았다.



그래서 재귀를 사용하지 않고 잘 모르는 부분인 DP를 활용하여 풀었다.

 이미 있는 점수들과 꺼내는 score의 가능한 조합을 살펴볼 때는 마지막까지 저장된 점수들의 길이 까지만 for 문을 돌려서 변수 t를 꺼내줘야 한다.

그렇지 않으면 마지막 append 부분에서 계속 추가되기 때문에  for 문이 멈추지 않는다.



dp는 분할정복과 비슷하지만 작은 문제의 중복이 일어나는지 일어나지 않는지에 차이가 있다.

dp는 모든 작은 문제를 한번만 풀어야 하고 정답은 구한 작은 문제는 메모(저장)을 해놓는다.



```python
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    score_list = list(map(int, input().split()))

    # 가능한 점수의 부분집합들
    total_list = [0]
    # 0점은 자동으로 가능하므로 1을 할당
    check = [1] + [0] * sum(score_list)

    # 1. 점수를 꺼내면서 이미 구한 부분점수들과 조합을 해줌
    for score in score_list:
        end = len(total_list)
        # 1-2. 현재 있는점수까지만 해야함 (밑에서 append 하기 때문에 계속 추가됨)
        for t in total_list[:end]:
            # 1-3. 만약 이미 그 점수가 있다면 제외시킴(중복x)
            if not check[score+t]:
                # 1-4. 방문을 기록
                check[score+t] = 1
                # 1-5. 가능한 부분집합들에 추가해줌 
                total_list.append(score+t)

    # print(total_list)
    ans = len(total_list)
    # 2. 결과값 출력 
    print(f'#{tc} {ans}')

```







## #1244_최대상금

(완전탐색)



https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD



![image-20210414230153798](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210414230153798.png)![image-20210414230213506](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210414230213506.png)



시간초과를 피하려면 어떻게 풀어야 할 지 잘 모르겠어서 다른 사람들의 풀이를 참고했다.

경우의 수를 돌려주며 최대값이 나올 때마다 기존 값과 대체 시켜주었다.

카운팅 횟수가 남았는데 이미 저장된 최대값이 나온다면 구성된 숫자들이 동일한 숫자들인지 확인해주고

만약 같은 숫자들이 아니라면 마지막 값들을 바꾸어주었다.



```python
# 1. 몇번 바꿨는지 세주면서 경우의 수를 돌린다
def dfs(idx, cnt):
    global result
    # 1-1. 바꿀 수 있는 횟수가 남았다면
    if cnt:
        # 1-3. 최대값이 나와도 내부에서 교체해줌
        if lst_num == max_lst:
            # 매개변수 할당 (동일값들로 되어있는지, 만약 동일값들이면 카운팅 남아도 바꿔줄 필요없음)
            c = 0
            for i in range(len(lst_num) - 1):
                if lst_num[i] == lst_num[i + 1]:
                    c = 1
            # 동일한 값이 없다면 카운팅이 남았을 때 결과가 달라지므로 남은 카운팅 횟수만큼 위치를 바꿔줌
            if c == 0:
                while cnt:
                    lst_num[-1], lst_num[-2] = lst_num[-2], lst_num[-1]
                    cnt -= 1
            # 마지막 값을 저장
            temp = int(''.join(lst_num))
            # 마지막 값이 기존값보다 크면 마지막 값을 출력해줌
            if result < temp:
                result = temp
            return
        # 1-2.
        else:
            for i in range(idx, len(lst_num) - 1):
                for j in range(i, len(lst_num)):
                    # 내 뒤에 값이 나보다 크면 교체시도
                    if int(lst_num[i]) < int(lst_num[j]):
                        lst_num[i], lst_num[j] = lst_num[j], lst_num[i]
                        # 카운팅 빼고 재귀 (만약 카운팅이 끝났다면 기존값과 비교해준다)
                        dfs(idx + 1, cnt - 1)
                        # 원상 복귀
                        lst_num[i], lst_num[j] = lst_num[j], lst_num[i]

    # (카운팅이 끝났다면 dfs는 여기로) 기존값과 비교
    else:
        temp = int(''.join(lst_num))
        if result < temp:
            result = temp
        return


T = int(input())

for tc in range(1, 1 + T):
    num, change = input().split()

    # 0. 순회를 위해서 리스트 변환
    lst_num = list(num)
    change = int(change)
    # 0. 최대값 저장
    max_lst = sorted(lst_num)[::-1]
    result = 0
    # 1. dfs로 경우의 수를 찾아줌
    dfs(0, change)

    print(f'#{tc} {result}')
```





## #5188_최소합

(완전탐색)

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT





![image-20210415160930191](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210415160930191.png)

![image-20210415160943629](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210415160943629.png)





완전탐색을 이용하여 가능한 모든 경로를 살피고 경로를 이동하면서 그 위치의 인덱스를 더해서 

도착점에 도착했을 때 최소합이 되는 경로를 찾는 문제이다.

델타이동의 사용이 간간이 하다보니 아직 숙달은 안되었었다.



방문여부를 체크는 하는데 다시 빼줄 생각을 못해서 도착점으로 가지 않아서 1차로 헤매었다.



2차로는 경로를 구하긴 했는데 테케는 맞지만 시간초과 오류가 떠서 10개중 7개만 맞았다.

모든 경우를 구하면 안되고  이미 전에 구해진 경로의 총합보다 커졌다면 탐색 중간에라도 그만 가는게 맞다.(효율적이다?)

 알고리즘은 생각할 게 많다 



```python
# 3. 갈 수 있는 범위인지 확인해주는 함수
def IsSafe(col, row):
    return 0 <= col < n and 0 <= row < n


# 2. 아래 오른쪽을 재귀로 이동 (깊이 우선 탐색)
def BottomRight(col, row):
    global temp

    # 이미 마지막 총합보다 커졌으면 여기까지.. (없으면 시간초과)
    if route[-1] < temp:
        return

    # 마지막값에 도달했다면 그때의 총합을 저장
    if col == n-1 and row == n-1:
        route.append(temp)
        return
    # 하하하 우우우
    for dir in range(2):
        n_col = col + dc[dir]
        n_row = row + dr[dir]
        # 가능한 범위고 아직 안갔더라면 진행
        if IsSafe(n_col, n_row) and (n_col, n_row) not in visited:
            # 방문체크
            visited.append((n_col, n_row))
            # 그 지점의 값 더하기
            temp += lst[n_col][n_row]
            # 다시 우 하 로 이동하는 함수 실행
            BottomRight(n_col, n_row)
            # 여기까지만 해주면 도착점은 이미 갔던곳이라서 다시 안감
            # 방문한곳과 그 위치의 값들을 삭제
            visited.remove((n_col, n_row))
            temp -= lst[n_col][n_row]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    # 0. 방문여부와 최종합들을 담을 빈 리스트 할당
    visited = []
    route = [9999]
    # 0. 초기값 할당
    temp = lst[0][0]
    # 아래 오른쪽 순으로 이동
    dc = [1, 0]
    dr = [0, 1]
    # 1. 아래 오른쪽으로 돌면서 마지막까지 가는 모든 경로를 구해주는 함수
    BottomRight(0, 0)

    # print(route)
    # print(len(route)) #7,6,9 vs 15 25 51
    # 4. 가본 경로중에 가장 최소값 찾기 (생략)
    # min_route = min(route)
    # min_route = merge_sort(route)[0]
    # print(f'#{tc} {min_route}')

    # 5. 결과값 출력 (가장 마지막 인덱스가 최소값이다)
    print(f'#{tc} {route[-1]}')
```







## #5189_전자카트

(완전탐색)

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT

![image-20210415175213778](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210415175213778.png)![image-20210415175229512](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210415175229512.png)

첫값과 마지막값은 항상 고정되어 있으므로 

인덱스 1을 제외한 숫자들로 순열을 구해서 총합을 구해주었다.

더 빠르게? 하려면 총합을 구할 때 이미 전 총합보다 크다면 그만 구해주는 조건을 집어넣으면 좋을 것 같다.



```python
# 3. 머지소트(병합정렬)
def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        mid = n //2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        new_arr = []
        l = r = 0
        while l < mid and r < n - mid:
            if left[l] < right[r]:
                new_arr.append(left[l])
                l += 1
            else:
                new_arr.append(right[r])
                r += 1
        return new_arr + left[l:] + right[r:]


# 2. 만든 순열을 사용해 해당 위치의 값 더해주기
def GolfArea(arr):
    # 첫번째 값과 마지막값은 초기에 넣어줌
    temp = area[0][arr[0]] + area[arr[-1]][0]
    # 순열 돌린거 집어넣으며 임시변수에 더해주기
    for i in range(len(arr)-1):
        temp += area[arr[i]][arr[i+1]]
    # 총합 리스트
    total.append(temp)


# 1. 순열만들기
def perm(idx, length):
    # 전체 길이만큼 왔으면 해당 위치의 값을 더해주는 함수 실행
    if idx == length:
        # print(arr)
        GolfArea(arr)
    # 자리를 바꿔주며 순열을 만듦
    else:
        for change in range(idx, length):
            arr[idx], arr[change] = arr[change], arr[idx]
            perm(idx+1, length)
            arr[idx], arr[change] = arr[change], arr[idx]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 2차원리스트의 골프장
    area = [list(map(int, input().split())) for _ in range(n)]
    # 0. 첫번째 값을 제외하고 순열 고고
    arr = [i for i in range(1, n)]
    # 0. 배터리 소비량의 총합을 담을 리스트
    total = []
    # 1. 순열돌리는 함수 실행
    perm(0, n-1)

    # 3. 병합정렬후 가장 작은 최소값 저장
    min_total = merge_sort(total)[0]
    # 4. 결과값 출력
    print(f'#{tc} {min_total}')
```





## #5201_컨테이너운반

(그리디)

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT



![image-20210416000135171](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210416000135171.png)

![image-20210416000142533](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210416000142533.png)



내림차순으로 정렬하고 차례로 비교해주면서 실을수 있다면 싣고 그 값을 제거해준다.



```python
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 1. 크기순으로 화물무게와 트럭 적재용량을 세운다 (내림차순)
    weight = sorted(weight)[::-1]
    truck = sorted(truck)[::-1]
    # 2. 실리는 화물 리스트
    load = []

    for i in range(n):

        for j in range(len(truck)):
            # 운반 가능한 무게면 append
            if weight[i] <= truck[j]:
                load.append(weight[i])
                # 운반후에 그 트럭은 remove
                truck.remove(truck[j])
                break
    # 3. 결과 값 출력
    print(f'#{tc} {sum(load)}')

```



## #5103_베이비진 게임

(그리디)



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT



![image-20210416003914916](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210416003914916.png)



run 체크할 때 (lst[i] and lst[i+1] and lst[i+1]) >= 1

이라고 해서 테케 1번이 2로 나와서 왜그러나 싶었다. 



run 변수가 있으면 코드 제출이 되지 않았다..



```python
# 2. 체크하는 함수
def check(lst):
    global runs, triplet
    for i in range(len(lst)):
        # 세게면 트리플렛
        if lst[i] == 3:
            triplet += 1
        # 인덱스가 마지막 두개가 아니라면 run 체크
        if i < len(lst)-2:
            if (lst[i] and lst[i+1] and lst[i+2]) >= 1:
                runs += 1
    # run이나 triplet이 있다면 승리
    if runs or triplet:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    runs = 0
    triplet = 0
    player1 = [0]*10
    player2 = [0]*10
    ans = 0

    # 1. 플레이어1과 2에게 돌아가면서 카드주기
    for i in range(12):
        if i%2 == 0:
            player1[card[i]] += 1
            # 한장 줄 때 마다 체크, 만약 run이나 triplet이 있다면 멈춘다
            if check(player1):
                ans = 1
                break
        else:
            player2[card[i]] += 1
            # 한장 줄 때 마다 체크, 만약 run이나 triplet이 있다면 멈춘다
            if check(player2):
                ans = 2
                break
    # 3. 결과출력
    print(f'#{tc} {ans}')


```



## #2819_격자판에 숫자 이어 붙이기



https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB



![image-20210417010407777](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210417010407777.png)

![image-20210417010417088](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210417010417088.png)



알고리즘 풀면 시간이 참 잘간다.. 

푸는 속도가 오래 걸리는 덕이다.



잠깐 설명들은대로 dc dr을 만들지 않고 함수안에 i+1, i-1을 넣어 조정해주려고 하였는데 답이 잘 나오지 않아서 델타이동을 사용해 풀었다.

만약  set함수를 쓰지 않는다면 시간이 10배 이상 걸려서 그만큼 set함수가 유용하다는 것을 알게 되었다..



백트래킹과 dfs 둘다 재귀 호출 형태로 구현되어 차이점이 헷갈렸는데, 두 알고리즘은 사용목적에 차이가 있고 

백트래킹은 일단 가보고 후보해가 되지않으면 다음 단계로 진행하지 않는다.

반면 dfs는 완전탐색을 기본으로 하는 그래프 순회 기법으로 모든 노드를 방문한다.



```python
# 3. 해당 위치를 포함해 더해가면서 7개가 되면 셋에 더해주는 함수 실행
def make_seven(n, c, r):
        global unique
        if len(n) == 7:
            # 셋 함수에 더하기 
            unique.add(n)
            return
        # 델타이동을 해주며 사방면 탐색
        for dir in range(4):
            n_col, n_row = c + dc[dir], r + dr[dir]
            # 지정된 범위 내에서라면 실행
            if 0 <= n_col < 4 and 0 <= n_row < 4:
                make_seven(n+grid[n_col][n_row], n_col, n_row)


T = int(input())
for tc in range(1, T+1):
    # 0. 이차원 리스트
    grid = [list(input().split()) for _ in range(4)]
    # print(grid)
    # 1. set함수로 중복을 막아준다.
    unique = set()
    dc = (0, 0, -1, 1)
    dr = (-1, 1, 0, 0)
    # 2. 모든 곳을 한번씩 방문하여준다.
    for c in range(4):
        for r in range(4):
            # 3. 해당 위치를 포함해 더해가면서 7개가 되면 셋에 더해주는 함수 실행
            make_seven(grid[c][r], c, r)
    # 4. 결과값 출력
    print(f'#{tc} {len(unique)}')




# set을 쓰지 않으면 시간 10배 더 걸림

#
# def make_seven(n, c, r):
#     global route
#     # route += grid[c][r]
#     if len(n) == 7:
#         if n not in emp:
#             emp.append(n)
#         return None
#     for dir in range(4):
#         n_col, n_row = c + dc[dir], r + dr[dir]
#         if 0 <= n_col < 4 and 0 <= n_row < 4:
#             make_seven(n + grid[n_col][n_row], n_col, n_row)
#             # route = route[::-1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     grid = [list(input().split()) for _ in range(4)]
#     # print(grid)
#     emp = []
#     route = ''
#     # unique = set()
#     dc = (0, 0, -1, 1)
#     dr = (-1, 1, 0, 0)
#     for c in range(4):
#         for r in range(4):
#             make_seven(grid[c][r], c, r)
#
#     print(f'#{tc} {len(emp)}') #16488
```





## #5204_병합정렬



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT



![image-20210419142542522](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210419142542522.png)![image-20210419142600381](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210419142600381.png)



몇번 해봤던 병합정렬인데 조금 헷갈렸다..

길이가 2미만 일 때 return 값에 n을 안 넣어놔서 정렬이 안되었었다.

정렬시켜줄 때 남은 거 더해주는 방법은 if else문으로 분기해도 되고 그냥 return에서 한번에 더해주어도 된다.



```python
# 1. 병합정렬로 정렬된 리스트만들기
def merge_sort(n):
    global cnt
    # 1-1. 길이가 2보다 작다면 그 값을 반환
    if len(n) < 2:
        return n
    # 1-2. 길이가 2이상이라면 2보다 작을 때 까지 반으로 나눈다
    else:
        mid = len(n)//2
        N = len(n)
        left = n[:mid]
        right = n[mid:N]
        new_lst = []
        # 마지막까지 반으로 나누기
        left = merge_sort(left)
        right = merge_sort(right)

        # 1-3. 나눈값들을 인덱스 처음부터 비교해가면서 더 작은값 새로운 리스트에 더해주기
        l = r = 0
        # 1-4. 나눈값중에 왼쪽 끝값이 더 크다면 cnt로 세어주기
        if left[-1] > right[-1]:
            cnt += 1
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                new_lst.append(left[l])
                l += 1
            else:
                new_lst.append(right[r])
                r += 1

        # 1-5. 남은거 더해주기
        if l < len(left):
            new_lst.extend(left[l:])
        else:
            new_lst.extend(right[r:])

        # 1-6. 정렬된 리스트를 차례로 반환
        return new_lst
        # return new_lst + left[l:] + right[r:]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    # 1. 병합정렬로 정렬된 리스트만들기
    merge_lst = merge_sort(lst)

    # print(cnt)
    # lst[len(lst)//2]

    # 2. 병합정렬로 정렬된 리스트의 중간값
    mid_num = merge_lst[len(lst)//2]

    # 3. 결과값 출력
    print(f'#{tc} {mid_num} {cnt}')
```







## #5205_퀵정렬



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT



![image-20210419172120493](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210419172120493.png)



완성코드:



재귀없이 1회 퀵정렬

```python
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pibut = numbers[0]
    left = []
    right = []

    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        else:
            right.append(numbers[i])
    return [left, pibut, right]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    print(quick_sort(lst))
```



재귀적용

```python
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pibut = numbers[0]
    left = []
    right = []


    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        else:
            right.append(numbers[i])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return [sorted_left, pibut, sorted_right]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    print(quick_sort(lst))
```

출력:

[[[], 1, [1]], 2, [[], 2, [3]]]
[[[[[], 1, [[], 2, [3]]], 4, []], 5, [6]], 7, [[[8], 9, []], 10, []]]

대괄호 처리해줘야함.



테스트케이스 10개중 9개 성공

```python
# 1. 퀵소트 함수적용 
def quick_sort(numbers):
    # 길이가 1보다 작으면 숫자 반환 (빈 값도 고려)
    if len(numbers) <= 1:
        return numbers
    # 기준값은 첫번째 인덱스
    pibut = numbers[0]
    left = []
    right = []

    # 첫번째 인덱스를 기준으로 두번째부터 끝까지 pibut보다 작으면 왼쪽리스트로 같거나크면 오른쪽리스트로 append
    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        else:
            right.append(numbers[i])
            
    # 왼쪽 오른쪽으로 1회 정렬된 리스트를 첫번째 길이가 1보다 작거나같냐는 if문에 걸릴 때 까지 재귀
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    
    # 리스트로 출력하기 때문에 리스트 안에 대괄호 제거를 위해 *추가해서 결과 반환 
    return [*sorted_left, pibut, *sorted_right]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    # 1. 퀵소트 함수적용 
    sorted_lst = quick_sort(lst)
    
    # 2. 결과값 출력(중간값)
    print(f'#{tc} {sorted_lst[len(sorted_lst)//2]}')
```



파티션 적용..

왼쪽 원소들이 피봇보다 모두 작을 때와 그렇지 않을 때  잘 구분해서 조건 줘야함

모두작다면 그 이후인 right를 피봇으로 잡고 좌우를 정렬해준다

그렇지 않다면 left쪽의 큰값과 right쪽의 작은값을 스왑하고 왼쪽으로 이동한 right에서부터 피봇으로 정해주고 다시 소팅한다.

기존의 퀵소트에 파티션 개념이 들어갔는데 이해가 쉽지 않다 :sweat_smile:

```python
# 1. 퀵소트 함수적용
def quick_sort(numbers, s, e):
    # s가 e보다 커질 때 리턴
    if s >= e:
        return
    # 기준값은 중간인덱스
    pivot = (s+e)//2
    left = s
    right = e

    # 피봇보다 큰값과 피봇보다 작은 값을 찾을 때까지 left는 1 더해주고 right는 1 빼줌
    while left < right:
        while numbers[left] < numbers[pivot] and left < right:
            left += 1
        while numbers[right] >= numbers[pivot] and left < right:
            right -= 1

        if left < right:
            # 왼쪽원소들이 다 작을 때
            if left == pivot:
                # right가 피봇
                pivot = right
            # 큰 left와 작았던 right를 서로 교환
            numbers[left], numbers[right] = numbers[right], numbers[left]
    # 피봇과 right의 스왑
    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]

    # 새로운 피봇을 기준으로 좌우 퀵소트
    quick_sort(numbers, s, right-1)
    quick_sort(numbers, right+1, e)



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    # 1. 퀵소트 함수적용
    quick_sort(lst, 0, n-1)

    # print(lst)
    # 2. 결과값 출력(중간값)
    print(f'#{tc} {lst[n//2]}')


```





## #5207_이진탐색



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT



![image-20210420013843315](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420013843315.png)

![image-20210420013855742](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420013855742.png)





리스트들이 미리 정렬되어 있는지 확인해야 한다.

직전에 같은 방향을 탐색했는지 확인할 때는 하나의 변수로 체크하는게 안전하다..



```python
# 2. 이진탐색 함수
def binary_search(lst, num):
    # 초기값들
    left = 0
    right = n-1

    # is_left = False
    # is_right = False
    lr_check = 0

    result = 0
    # 둘이 만나기 전까지 반복
    while left <= right:
        mid = (left+right)//2
        # m값이라면 찾았으니 1을 반환
        if A[mid] == num:
            result = 1
            return result
        # 원소가 m보다 작다면 오른쪽을 이동시켜 left로 체크
        elif A[mid] > num:
            if lr_check == -1:
                return result
            # is_left = True
            lr_check = -1
            right = mid - 1


        # 원소가 m보다 크다면 왼쪽을 이동시켜 right 체크
        elif A[mid] < num:
            if lr_check == 1:
                return result
            # is_right = True
            left = mid + 1
            lr_check = 1
            # return binary_search(lst, num)
        else:
            return result

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0

    # 1. 두번째 리스트의 원소들을 차례로 이진탐색 함수에 넣어준다
    for i in B:
        # print(binary_search(A, i))
        # 1-1. 만약 리턴값이 1이라면 카운팅해준다
        if binary_search(A, i):
            cnt += 1
    # 3. 결과값 출력 
    print(f'#{tc} {cnt}')
```



## #5208_전기버스2



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT#



![image-20210420114339262](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420114339262.png)

![image-20210420114349374](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420114349374.png)



시간초과로 10개중 7개 맞은 코드

```python
def bus(st):
    global change

    for j in range(1, bat[st]+1):
        # print(i+j)
        change += 1
        if st+j >= bat[0]:
            if change_lst:
                if change_lst[-1] > change:
                    change_lst.append(change)
            else:
                change_lst.append(change)
            change -= 1
            return
        else:
            bus(st+j)
            change -= 1


T = int(input())
for tc in range(1, T+1):
    bat = list(map(int, input().split()))
    change = -1
    change_lst = []
    bus(1)


    # print(change_lst)
    print(f'#{tc} {change_lst[-1]}')
```





반복문을 돌릴 때 내림차순으로 바꾸고 리스트에 append 하는 방식이 아니라 값을 바꿔주는 방법으로 변경하였다.

유망하지 않은 길에 대해선 종료조건을 주어서 더 이상 가지 못하게 해주는게 중요하다.

```python
# 1. 백트래킹을 이용한 배터리 교체 함수
def bus(st):
    global change, result
    
    # 1-1. 이미 교환횟수가 기존값보다 크면 여기서 반환
    if result < change:
        return
    # 1-2. 도착했을때 기존값보다 작으면 결과값으로 반영
    if st >= bat[0]:
        if result > change:
            result = change
        return
    
    # 1-3. 갈 수 있는 최대지점부터 시작해서 방문 
    for j in range(st+bat[st], st, -1):
        change += 1
        bus(j)
        change -= 1


T = int(input())
for tc in range(1, T+1):
    # 0. 충전소 개수와 충전량들이 있는 리스트
    bat = list(map(int, input().split()))
    # 0. 첫 배터리 장착은 교환횟수에서 제외
    change = -1
    result = 9999
    # 1. 백트래킹을 이용한 배터리 교체 함수
    bus(1)
    
    # 2. 결과값 출력
    print(f'#{tc} {result}')
```





## #5209_최소생산비용



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT#



![image-20210420170548232](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420170548232.png)![image-20210420170604408](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420170604408.png)



방문으로 이전에 사용했었는지 체크하기 전에 인덱스로 어떻게 접근할 수 있을까 생각하다가 시간이 오래걸렸다...

방문을 체크하면 idx값을 한개씩 올려주면 이전의 열은 보지않게되고 

total값으로 새로운 인덱스의 값들중에 이전에 가지 않았던 행들로 가서 값을 쌓아간다.

같은 열이라도 다른 행으로 갈 수 있으므로 재귀로 함수에 들어갔다면 방문은 바로바로 지워줘야함.



```python
# 2. 중복되는 인덱스없이 최소비용을 구하는 함수
def minimum_cost(idx, total):
    global result
    # 이미 구한 값보다 크다면 리턴 
    if total > result:
        return
    # 길이만큼 재귀시켰으면 결과를 저장
    if idx == n:
        result = total
    # 길이만큼 돌면서 이 전에 인덱스에 방문안한값들만 재귀 
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            minimum_cost(idx+1, total+cost[idx][i])
            # 방문체크 지우기 
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    # 0. 방문을 체크하기 위한 리스트
    visited = [0 for _ in range(n)]
    result = 9999
    # 1. 중복되는 인덱스없이 최소비용을 구하는 함수
    minimum_cost(0, 0)
    
    # 3. 결과값 출력
    print(f'#{tc} {result}')
```





## #1865_동철이의 일 분배



https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc



![image-20210420182531256](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420182531256.png)

![image-20210420182540729](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420182540729.png)



재귀로 값을 계속 곱해 나갈 때, 이미 그 값이 그 전의 결과보다 크다고 해놓으면 

테케에서 시간초과가 난다.

크거나 같으면 반환시켜야지 테케를 모두 통과할 수 있다.



소수점 6째 자리까지 출력하기 위해서는 그냥 round를 쓰면 안되고 :.0.6f로 표현해야지 0인 숫자들도 모두 출력할 수 있다.



방문체크 기록하고 재귀를 돌리는 것은 위의 최소생산비용과 동일한 방식이다.



```python
import time
import sys
sys.stdin = open('input.txt')

start = time.time()

# 2. 가장 높은 확률 구해주는 함수
def solution(idx, total):
    global result

    # 이미 크거나 같다면 끝내주기 (같다를 주지 않으면 36번 테케에서 안 끝남)
    if total <= result:
        return
    # 사람수만큼 왔다면 결과값 저장
    if idx == n:
        result = total

    # 사람한명이 한명의 일을 가져가게 기록체크 재귀하고나선 기록 지우기
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            solution(idx+1, total*work[idx][i]*0.01)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # print(n)
    work = [list(map(int, input().split())) for _ in range(n)]
    # print(work)
    result = 0
    visited = [0 for _ in range(n)]
    # 1. 가장 높은 확률을 구해주는 함수 (곱셈이니 두번째 인덱스 total은 1)
    solution(0, 1)
    result = result*100

    # 3. 결과값 출력
    print(f'#{tc} {result:.6f}')
print("time :", time.time() - start)
```







## #2806_N_Queen



https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXd7Q4tqYs0DFAUO&contestProbId=AV7GKs06AU0DFAXB&probBoxId=AXd7RueqYu4DFAUO&type=PROBLEM&problemBoxTitle=



![image-20210420235119412](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420235119412.png)

![image-20210420235129709](C:\Users\a\알고리즘\.SWEA_README\4월 SWEA README.assets\image-20210420235129709.png)





 대각선 부분의 처리를 어떻게 하는지 이해하려고 여러번 생각하였다.

오른쪽 대각선 왼쪽 대각선 나눠서 행-열, 행+열 을 처리해주는 방법이 있고

그냥 둘 사이의 거리를 절대값으로 덮어주면 두 대각선 모두 처리 가능하였다.

그리고 방문의 기록을 row에 기록하지만 실제로는 이게 열에 같은 값이 있는지 체크해주는것이다.

말도 어렵고 이해하기도 어려운 문제이다 :joy:



```python
# 3. 대각선 체크 : 같은 대각선상에 있다면 x와 y의 거리의 절대값이 같다 한개라도 안겹치면 True로 반환된다 
def check(y, x):
    for i in range(y):
        if y - i == abs(x - diagonal[i]):
            return False
    return True


# 2. n까지 갔을 때 n개의 퀸을 놓는 경우를 세는 함수 실행
def n_queen(y):
    global cnt, result
    
    # 만약 n까지 갔고 퀸도 n개라면 
    if y == n and cnt == n:
        # 경우의 수 더하기 
        result += 1
        return
    
    # row에 x를 넣어가면서 같은 열에 이미 퀸이 있는지 체크
    for x in range(n):
        # 3. 대각선도 체크 
        if not visited[x] and check(y, x):
            # 열과 대각선에 체크 
            visited[x] = 1
            cnt += 1
            diagonal[y] = x
            # col (y)값 늘리고 재귀  
            n_queen(y+1)
            # 재귀후 원상복귀
            visited[x] = 0
            cnt -= 1
            diagonal[y] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())

    # 같은 열과 대각선의 정보를 담을 리스트
    visited = [0 for _ in range(n)]
    diagonal = [0 for _ in range(n)]

    cnt = 0
    result = 0
    # 1. n까지 갔을 때 n개의 퀸을 놓는 경우를 세는 함수 실행
    n_queen(0)
    
    # 4. 결과값 출력 
    print(f'#{tc} {result}')
```





## #5247_연산



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT&&#

**※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.**


자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


**[입력]**

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

**[출력]**

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 

입력

| 3 2 7 3 15 36 1007 |      |
| ------------------ | ---- |
|                    |      |

[sample_input.txt](https://swexpertacademy.com/main/common/contestProb/contestProbDown.do?downType=in&contestProbId=AWUS1FaKImUDFAVT&_menuId=AVtnUz06AA3w6KZN&_menuF=true)

출력

| #1 3 #2 4 #3 8 |      |
| -------------- | ---- |
|                |      |

[sample_output.txt](https://swexpertacademy.com/main/common/contestProb/contestProbDown.do?downType=out&contestProbId=AWUS1FaKImUDFAVT&_menuId=AVtnUz06AA3w6KZN&_menuF=true)



큐에는 초기에 배정된 숫자와 카운팅 변수를 집어넣는다.

카운팅변수는 다음 bfs 단계로 넘어가기전에 1씩 더해주고 큐에서 숫자와 카운팅을 pop할 때 이미 pop했던 값이면 continue로 아래의 계산을 수행하지 않게 해준다.

방문을 고려해주지 않으면 3개의 tc에서 통과하지 못하고

백만값을 정확히 제한해주지 않으면 4개의 tc에서 통과하지 못한다.



```python
from collections import deque
import sys

sys.stdin = open('input.txt')


# 2. bfs를 돌며 a에서 b만드는 연산
def bfs(a, b):
    global cnt
    q = deque()
    # 초기값
    q.append((a, 0))
    # 중복을 제거할 딕셔너리
    check = {}

    while q:
        num, cnt = q.popleft()
        # tc 3개-> 6개 이미 벨류가 있는 num 이라면 다음 회차 while q로 넘어간다. 
        if check.get(num):
            continue
        check[num] = 1
        if num == b:
            return cnt
        cnt += 1
        # 백만 넘게까지 주면 tc를 모두 통과하지 못함
        if 0 < num + 1 <= 1000000:
            q.append((num+1, cnt))
        if 0 < num - 1 <= 1000000:
            q.append((num-1, cnt))
        if 0 < num * 2 <= 1000000:
            q.append((num*2, cnt))
        if 0 < num - 10 <= 1000000:
            q.append((num-10, cnt))




T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    cnt = 0
    # 1. bfs를 돌며 b값이 되게 연산
    bfs(a, b)
    # 3. 결과값출력
    print(f'#{tc} {cnt}')
```







## #5248_그룹나누기



https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT&&#





**※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.**


수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.


**[입력]**

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M, 다음 줄에 M 쌍의 번호가 주어진다. 2<=N<=100, 1<=M<=100

**[출력]**

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 

입력



| 3 5 2 1 2 3 4 5 3 1 2 2 3 4 5 7 4 2 3 4 5 4 6 7 4 |      |
| ------------------------------------------------- | ---- |
|                                                   |      |



[sample_input.txt](https://swexpertacademy.com/main/common/contestProb/contestProbDown.do?downType=in&contestProbId=AWUS2OVaIpgDFAVT&_menuId=AVtnUz06AA3w6KZN&_menuF=true)

출력



#1 3 #2 2 #3 3

[	sample_output.txt ](https://swexpertacademy.com/main/common/contestProb/contestProbDown.do?downType=out&contestProbId=AWUS2OVaIpgDFAVT&_menuId=AVtnUz06AA3w6KZN&_menuF=true)



딕셔너리를 이용하려고 했는데 딕셔너리에 값을 추가해나가는게 어려워서 다른 방법을 찾다가  두개의 함수를 만들어 내가 지목한 사람의 인덱스에 나의 값을 넣고 set으로 중복 제거한 개수를 알아보는 방법으로 하였다.

마지막에 tc가 정답으로 안나와서 뭐를 놓쳤나 봤는데 내가 지목한 사람들과 같은 팀이 되고

내가 지목받은 사람들과 같은 팀이 되면,

내가 지목한 팀원과 나를 지목한 팀원의 연결이 안되어서 다시 find_set 함수를 통해 마지막에 바뀐 나의 팀까지 적용시켜주어야 했다.

그래프에 다시 입문한 느낌이다..



```python
# 3. 원래 인덱스는 그대로 이미 다른 팀에 속했으면 그 팀의 번호 가져오기
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

# 2. 내가 같은 팀 되고 싶은 사람 지목 (지목받은 사람의 인덱스에 내 번호 삽입)
def combine(go, to):
    parent[find_set(to)] = find_set(go)


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 팀을 정하는 신청서
    pair = list(map(int, input().split()))

    # 원래의 인덱스 번호를 저장
    parent = [0] * (n+1)

    # n이 아니라 n+1까지 해줘야 함
    for i in range(n+1):
        parent[i] = i

    # 1. 짝수번호는 자신 홀수는 같은 팀이 되고 싶은 사람
    for i in range(m):
        go = pair[i*2]
        to = pair[i*2+1]
        # 내가 선택한 사람들과 같은 팀 되기 함수 실행
        combine(go, to)

    sp = set(parent)

    # 4. 이 작업을 해줘야 자신을 선택한 사람과 내가 선택한 사람들이 같은 팀이 됨
    result = []
    for i in range(len(parent)):
        result.append(find_set(i))
    result = set(result)

    # 5. 맨 앞에 0을 제외한 결과 출력 
    print(f'#{tc} {len(result)-1}')
```





## #5251_최소이동거리







다익스트라 이해가 잘 안가서 다른거랑 섞어서 쓰다가 테케 2개가 안맞았는데 어찌하다가 1개만 안맞고 다른건 맞습니다..

하지만 이해가 잘 안갑니다.. 

플로이드 와샬은 간단하게 구현되어 있던데 다익스트라는 조금 더 노력해보겠습니다



```python
from heapq import heappop, heappush

# 10개중 8개 성공
import sys
sys.stdin = open('input.txt')


# 2. 다익스트라 함수 실행
def dijkstra(s, d):
    global gragh, a
    # n = len(gragh)
    table = [INF for i in range(n+1)]
    table[s] = 0
    pq = [(0, 0)]
    visited = [0 for _ in range(n+1)]
    # print(gragh)
    while pq:
        d, idx = heappop(pq)

        if visited[idx]:
            continue

        visited[idx] = 1
        for a, b in gragh[idx]:
            if b + d < table[a]:
                table[a] = b + d
                heappush(pq, [table[a], a])

    return table[a]


T = int(input())
for tc in range(1, T+1):
    n, e = map(int, input().split())
    # nodes = [list(map(int, input().split())) for _ in range(e)]
    # node = [[] for _ in range(n + 1)]
    INF = int(1e9)

    # 1. 주어진 s, e, w 를 이용하여 그래프를 그립니다
    gragh = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = list(map(int, input().split()))
        gragh[a].append((b, c))
    # print(gragh)

    # 2. 다익스트라 0부터 n까지 거리를 구해줍니다.

    # 3. 결과값 출력
    dist = dijkstra(0, n)
    # for i in range(1, n):
    #     dist = min(dist, dijkstra(0, i) + dijkstra(i, n))

    print(f'#{tc} {dist}')
```



