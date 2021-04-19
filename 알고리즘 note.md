[toc]

# :notebook_with_decorative_cover: 알고리즘 note



## 1.  정렬 알고리즘



정렬 알고리즘의 시간 복잡도 정리

![image-20210408204502496](C:\Users\a\Desktop\typora\aidenrism_daily\알고리즘 note.assets\image-20210408204502496.png)

간단하지만 비효율적인 방법 : 삽입정렬, 선택정렬, 버블정렬

복잡하지만 효율적인 방법: 퀵정렬, 힙정렬, 합병정렬, 기수정렬



> https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html

> 빅오 O() -> 최악의 시간, 오메가 -> 최상의 시간, 세타 -> 평균시간



---

1. **선택정렬**
   - 선택정렬의 시간복잡도는 O(n^2)
   - 정렬되지 않은 데이터들에 대해 가장 작은 데이터를 찾아 가장 앞의 데이터와 교환해나가는 방식.
   - 1. 앞에서부터 데이터 한개를 선택
     2. 선택한 데이터 이후에 있는 원소들 중 가장 작은 값 탐색
     3. 선택한 값과 변경
   - 불안정 정렬이다.

파이썬 코드

```python
import random

a = random.sample(range(1, 100), 10) 
print(a)# 정렬 전 리스트
print('')
for i in range(len(a)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(a)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if a[i] > a[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            a[i] , a[j]  = a[j], a[i] # swap 해주기
print('')
print(a) # 정렬 후 리스트

# 출력
# [43, 49, 33, 3, 64, 19, 47, 20, 77, 86]


# [3, 19, 20, 33, 43, 47, 49, 64, 77, 86]
```



---

2. **삽입정렬** 
   - 삽입정렬의 시간복잡도는 O(n^2)
   - 삽입정렬은 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘.
   - 1. 삽입 정렬은 두 번째 자료로부터 시작하여 그 앞의 자료들과 비교하여 삽입할 위치를 지정한 후 자료를 옮기고 지정한 자리에서 자료를 삽입하여 정렬하는 알고리즘
   - 장점 : 구현이 간단하다
   - 단점: 배열이 길어 질수록 효율이 떨어진다.
   - 최악의 경우 시간 복잡도가 O(n^2)이지만 최적의 경우 한번씩 밖에 비교를 안하므로 O(n)이다.



```python
for i in range(1, len(a)): # 리스트의 크기만큼 반복
    for j in range(i, 0, -1): # j 인덱스의 값이 줄어드면서 삽입할 위치를 찾을 때까지 반복
        if a[j] < a[j-1]: # 현재 인덱스가 앞의 원소보다 작다면
            a[j], a[j-1] = a[j-1], a[j] # swap해서 값 뒤로 밀어내기
        else : break # 불필요한 반복을 피하기 위해 break
print('')
print(a)# 정렬 후 리스트 출력

#출력
[8, 9, 3, 1, 6]


[1, 3, 6, 8, 9]
```



---

3. **버블정렬**
   - 안정정렬이다. 모든 원소를 하나하나 비교하여 스왑하는 작업을 반복한다.
   - 시간복잡도는 O(n^2)이다.
   - 장점: 구현이 간단하다
   - 단점: 하나의 요소가 가장 왼쪽으로 이동하기 위해서 배열의 자료동작업을 할

```python

for i in range(1, len(a)): # 리스트의 크기만큼 반복
    for j in range(i, 0, -1): # j 인덱스의 값이 줄어드면서 삽입할 위치를 찾을 때까지 반복
        if a[j] < a[j-1]: # 현재 인덱스가 앞의 원소보다 작다면
            a[j], a[j-1] = a[j-1], a[j] # swap해서 값 뒤로 밀어내기
        else : break # 불필요한 반복을 피하기 위해 break
print('')
print(a)# 정렬 후 리스트 출력

#출력
[8, 9, 3, 1, 6]


[1, 3, 6, 8, 9]
```

---

4. **퀵정렬**
   - 불안정 정렬
   - 평균적으로 빠른 수행속도
   - 분할정복 알고리즘의 하나로 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬방법, 합병정렬과 달리 퀵정렬은 라스트 리스트를 비균등하게 분할한다.
   - 1. 리스트 안에 한 요소를 선택한다 (피벗) 요소보다 작은 값은 9000이다.
     2. 피벗 기준으로 
     3. 분할 리스트들이 더 이상  불가능 할 때 까지 
   - 재귀 함수를 통해 구현되며, 데이터 양이 n배 많아 진다면 실행시간은 b배 보다 조금 더 많아짐 (정비례 하지는 않는다)


```python
import random 

a = random.sample(range(1, 10), 5)
print(a) # 정렬 전 리스트
print('')
def quickSort(a, start, end):# 재귀함수용 함수 선언(리스트, 시작인덱스, 종료인덱스)
    # print(a)
    if start < end: # 시작 인덱스 보다 끝 인덱스가 클 경우
        left = start # left 변수에 시작 인덱스 할당
        pivot = a[end] #  //pivot 값은 a리스트에 마지막 원소 값
        for i in range(start, end): # 시작인덱스부터 끝 원소까지 반복
            if a[i] < pivot: # 리스트 인덱스 값이 pivot 값보다 작을 경우라면
                a[i], a[left] = a[left], a[i] #  해당 인덱스와 left인덱스  swap
                left += 1 # 인덱스 하나 증가 시켜주기(자리를 옮겨가며 비교해야 하기 때문에)
        a[left] , a[end] = a[end], a[left] # left인덱스와 끝 인덱스 swap
        print(left)
        quickSort(a, start, left-1) # 재귀 호출 (리스트, 시작 인덱스, left-1)
        quickSort(a, left+1, end) # 재귀 호출 (리스트, left+1, 종료인덱스)
quickSort(a, 0, len(a)-1)
print('')
print(a) # 정렬 후 리스트

#출력
[8, 1, 7, 2, 5]


[1, 2, 5, 7, 8] 
```



---

5. **병합정렬**

   - nlogn의 시간 복잡도

   - 일반적으로 안정정렬에 속하며 분할 정복 알고리즘의 하나이다.

     (분할정복 방법: 문제를 작은 2개의 문제로 분리하고 각각 해결한 다음 결과를 모아서 원래 문제를 해결하는 전략, 대개 분할정복은 재귀를 통해 구현됨)

   - 1. 리스트 길이가 1 이하이면 이미 정렬된 것
     2. 정렬되지 않은 리스트를 반으로 자른다.
     3. 길이가 한개가 될 때 까지 자른다
     4. 각 부분을 재귀적으로 합병정렬을 이용해 정렬한다
     5. 두 부분의 리스트를 다시 정렬된 리스트로 합병한다.

   - 안정적인 정렬방법이다.

   - 데이터 분포에 영향을 덜 받는다. 입력 데이터가 무엇이던간에 정렬되는 시간이 동일하다.

```python
import sys
sys.stdin = open('input.txt')


def merge_sort(numbers):
    N = len(numbers)
    # base case => numbers 의 길이가 2보다 작다면(0, 1) 그대로 리턴
    if N < 2:
        return numbers
    
    # 중간점 잡기
    mid_idx = N // 2
    # 중간점 기준 왼쪽 리스트
    left = numbers[:mid_idx]
    # 중간점 기준 오른쪽 리스트
    right = numbers[mid_idx:]

    # 정렬된 왼쪽
    sorted_left = merge_sort(left)
    # 정렬된 오른쪽
    sorted_right = merge_sort(right)

    # 최종 병합된 결과
    merged = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        # 좌/우 맨 앞에서 더 작은 값을 최종 결과에 추가
        if sorted_left[l] < sorted_right[r]:
            merged.append(sorted_left[l])
            l += 1
        else:
            merged.append(sorted_right[r])
            r += 1
            
    # 좌/우 남은 숫자들은 이미 정렬되어 있으므로, 그대로 병합
    merged += sorted_left[l:]
    merged += sorted_right[r:]

    return merged


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {merge_sort(arr)}')

```



---



## 2. 백트래킹 vs DFS



0. 백트래킹이란 ?

   솔루션을 찾는 과정에서, 유망하지 않은 후보해에 대해 빠르게 포기하고 이전 단계로 되돌아(back track)가 다른 후보해를 찾는 알고리즘 기법

   

1. Backtracking과 DFS



​		백트래킹: 일단 가보고 후보해가 될 수 없으면 다음 단계로 진행하지 않고 되돌아 나온다.

​		DFS: 완전 탐색을 기본으로 하는 그래프 순회 기법으로, 모든 노드를 방문하는 것을 목표로 한다.



​		둘다 재귀 호출 형태로 자주 구현이 되어 헷갈릴 수 있다.

​		두 알고리즘은 사용 목적에 차이가 있다.

![image-20210417002501875](C:\Users\a\Desktop\eduaiden_lec\TIL\알고리즘 note.assets\image-20210417002501875.png)

1. 현재 트리에 대해 DFS를 수행 (단어가 일치하거나, 모든 노드를 방문할때까지 진행)
2. 가지 치기(pruning)를 통해 적합하지 않은 부분 제거 (위 그림에서는 AN, AIM)
3. 가지 치기한 결과 트리에 대해 1과정 다시 진행



2. 가지치기(Pruning)

   불필요한 탐색 부분을 제거하는 방법 

   트리 구조에서 나무 가지를 치듯이 가망성이 없는 부분을 제거해 나가는 것

3.  유망성(Promising)

   가망이 있는가 없는가를 따지는 기준



4. 백트래킹의 목표

   상태 공간 트리를 DFS로 탐색하여 해결 상태를 도달하는데 있어 불필요한 탐색을 하지 않는 것을 목표로 한다.

   조합의 문제에서 상태공간을 효과적으로 줄일 수 있다.



