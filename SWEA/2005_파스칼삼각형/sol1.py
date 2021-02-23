
N = 4

def pascal(n):
    f = [[1]]

    emp = []
    for i in range(0, n):
        emp += pascal(i)
        f += [emp,',' ]

    return f[n-1]

print(pascal(3))

# def fibo2(n):
#     f = [0, 1]
#
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#
#     return f[n]

