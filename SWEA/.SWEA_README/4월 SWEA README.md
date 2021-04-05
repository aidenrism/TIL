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
        # 방문할 왼쪽이 없다면 그 노드를 출력
        print(word[int(n)], end=' ')
        # 출력후 부모노드로 간 뒤 오른쪽 값을 방문 
        inorder(right[int(n)])

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
```

