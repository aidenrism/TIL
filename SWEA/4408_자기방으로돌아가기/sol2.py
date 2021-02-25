import sys
sys.stdin = open('input.txt')



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