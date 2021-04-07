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





