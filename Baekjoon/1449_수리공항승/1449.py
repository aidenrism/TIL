import sys
sys.stdin = open('input.txt')

# 물이 새는 곳의 개수 N, 테이프의 길이 L
N, L = map(int, input().split())
# 물이 새는 곳의 위치
location = list(map(int, input().split()))

# 누수 파이프의 정렬이 안되어있음을 가정하고 정렬함수를 만들어 정렬을 해줌
def my_sort(x):
    for j in range(len(x)):
        for i in range(len(x)-1):
            if x[i+1] < x[i]:
                x[i], x[i+1] = x[i+1], x[i]
    return x

# test11 = [333, 1, 3, 2, 5, 9, -1, 2]
# print(my_sort(test11))

# 위치들을 정렬해줌
my_sort(location)

# 테이프 counting 초기값
count = 1

# max함수를 만들어줌 
def my_max(x):
    if len(x) == 0:
        return 0
    else:
        bigger = x[0]
        for i in range(len(x)):
            if x[i] > bigger:
                bigger = x[i]
                continue
        
    return bigger

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