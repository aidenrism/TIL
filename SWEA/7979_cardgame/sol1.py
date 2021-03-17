import sys
sys.stdin = open('input.txt')

T = int(input())

# 회전 한 뒤에 중력으로 벽돌이 아래 깔린다
# 낙차가 가장 큰 상자를 구하는것
# 입력값에서 가장 마지막 값이 쌓인다 마지막값보다 앞에 있는 값들이 적을 때 그 마지막 길이만큼 낙차가 발생한다
# 가장 마지막 블럭을 기준으로 그거보다 더 길면 초기화가 되고 짧으면 짧은 줄 만큼 1씩 더해줌

# 우선 받은 값들을 리스트로 만들어야 함

for i in range(T):
    numbers = input()
    print(numbers)