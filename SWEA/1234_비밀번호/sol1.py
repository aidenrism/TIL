import sys
sys.stdin = open('input.txt')

def realnum(password):

    i = 1
    while len(password) > 1:
        if i >= len(password):
            break
        current = password.pop(-i)
        if current == password[-i]:
            password.pop(-i)
            if i > 1:
                i -= 1
        else:
            if i == 1:
                password.insert(len(password), current)
            else:
                password.insert(-i+1, current)
            i += 1

    return ''.join(password)

for tc in range(1, 11):
    n, password = input().split()

    emp = []
    for i in password:
        emp.append(i)

    print('#{} {}'.format(tc, realnum(emp)))