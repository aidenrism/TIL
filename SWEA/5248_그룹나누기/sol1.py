import sys
sys.stdin = open('input.txt')


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
