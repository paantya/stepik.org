import numpy as np


# Cкалярное произведение векторов
def scal(x, y): return np.sum([i_*j_ for i_, j_ in zip(x, y)])


n, m = map(int, input().split())
a_ = [[int(j) for j in input().split()] for _ in np.arange(n)]

a = np.array(a_, np.float128)
a0 = np.zeros((m, m+1), np.float128)
f = np.array(a[:, -1], np.float128)
e = np.array(a[:, :-1], np.float128).T

# формируем матрицу из скалярных произведений
for i in np.arange(m):
    for j in np.arange(m):
        a0[i][j] = scal(e[i], e[j])
    a0[i][m] = scal(f, e[i])

# Прямой ход метода Гауса
for i in np.arange(m):
    for j in np.arange(i+1, m):
        ak = a0[j][i]
        for k in np.arange(i, m+1):
            a0[j][k] = a0[j][k] - a0[i][k] * ak / a0[i][i]

# Обратный ход метода Гаусcа
for i in np.arange(m-1, -1, -1):
    for j in np.arange(i-1, -1, -1):
        ak = a0[j][i]
        for k in np.arange(i, m+1):
            a0[j][k] = a0[j][k] - a0[i][k] * ak / a0[i][i]

# Добиваемся того,что бы в a0[i,m] были решения МНК
for i in np.arange(m):
    a0[i][m] /= a0[i][i]

print(*a0[:, m], sep=' ')
