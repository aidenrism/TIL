import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pipe = input()
    cnt = 0
    emp = []
    for i in range(len(pipe) - 1):
        if pipe[i+1] == pipe[i] and pipe[i] == '(':
            cnt += 1
        elif pipe[i-1] == pipe[i] and pipe[i] == ')':
            cnt -= 1
        if pipe[i] != pipe[i+1] and pipe[i] == '(':
            emp.append(cnt)
        if pipe[i-1] != pipe[i] and pipe[i] == ')':
            back_cnt = 0
            for j in range(1, len(pipe)-i):
                if pipe[i+j] == ')':
                    back_cnt += 1
                else:
                    break
            emp.append(back_cnt)

    emp_cnt = 0
    for k in range(len(emp)):
                emp_cnt += emp[k]
    print('#{} {}'.format(tc, emp_cnt))


# pipe = '()(((()())(())()))(())'

# laser = 0
# for i in range(len(pipe)-1):
#     # for p in pipe:
#     if pipe[i] != pipe[i+1]:
#         laser += 1
# laser = int((laser-1)/2)
# print(laser)
# print(len(pipe))

