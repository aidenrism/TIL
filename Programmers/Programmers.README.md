[toc]

# Programmers 문제풀이





## #72413_합동택시요금 

- **문제 사이트** :

  -  백준
  -  Programmers
  -  SWEA

- **난이도**:

  - 어려움

- **사용한 알고리즘**

  - 플로이드 와샬

- **어려웠던 점**:

  - 다익스트라에 대한 이해가 안된상태에서 문제를 푸려고 하다보니까 어려웠다..
  - 풀이들을 보면서 이해하려고 했는데 그 중 플로이드 와샬이 이해하기가 쉬웠다.

- **Reference** :

  - https://programmers.co.kr/learn/courses/30/lessons/72413

-  **etc**:





## #67259_경주로 건설



- **문제 사이트** :
  -  백준
  -  Programmers
  -  SWEA
- **난이도**:
  - lv3
- **사용한 알고리즘**
  - bfs
- **어려웠던 점**:
  - 조건을 어디선가 잘못줘서 에러를 해결하지 못하였는데 다른 사람들의 풀이를 참고하여 방향에 대한 좋은 팁들을 알 수 있었다.
- **Reference** :
  - https://programmers.co.kr/learn/courses/30/lessons/67259
- **etc**:
  - 새로운 문제를 계속 푸는것보다 기존에 푼 것을 복습하는 시간도 가져봐야겠다.





## #72414_광고삽입

kakao blind test 문제이다



- **어려웠던 점**:
  - 구간을 어떻게 체크할 것 인가.. 에서 부터 막혀서 손도 대기 힘든 문제였다..
- **Reference** :
  - https://programmers.co.kr/learn/courses/30/lessons/72414
- **etc**:
  - 새로운 풀이를 알게 되어서 좋았습니다.
  - 다른 사람들의 풀이와 공식 해설을 참고하였습니다.
  - 어렵지만 새로운 접근법을 배운다면 더 쉬운 문제가 나올 때 응용해보기 좋을 것 같습니다.



```python
def solution(play_time, adv_time, logs):
    # 1. 문자열 입력값을 초로 변환
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)


    # 2. 구간별 배열
    all_time = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    # 3. 구간별 시청자 수 구하기
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    # 4. 구간별 시청자 수의 누적합 구하기
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    # 5. 플레이 타임동안 누적 시청자 수의 최대값인 구간 구하기 
    most_view = 0
    max_time = 0
    for start_time in range(1, play_time):
        if start_time + adv_time < play_time:
            end_time = start_time + adv_time
        else:
            end_time = play_time
        sum_played = all_time[end_time] - all_time[start_time]
        if most_view < sum_played:
            most_view = sum_played
            max_time = start_time + 1
    # 최대값 반환 
    return int_to_str(max_time)


# 1-1. 문자열을 숫자로 변환하는 함수
def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# 5-1. 숫자를 문자열로 변환하는 함수 
def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s
```

