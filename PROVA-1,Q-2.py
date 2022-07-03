import random
def somaMatrizes(a, b):
    c = []
    print('Soma entre as matrizes:')
    for s in range(0, n):
        print(a[s])
    print('-'*30)
    for s1 in range(0, n):
        print(b[s1])
    print('É a matriz:')
    for saida in range(0, n):
        c.append([0] * n)
        for sa in range(0, n):
            c[saida][sa] = a[saida][sa] + b[saida][sa]
        print(c[saida])

n = int(input('Quantos linhas e colunas teram suas matrizes?: '))

a = []
b = []

for linhas in range(0, n):
    a.append([])
    for colunas in range(0, n):
        valores2 = random.randint(1, 10)
        a[linhas].append(valores2)

for linhas1 in range(0, n):
    b.append([])
    for colunas1 in range(0, n):
        valores2 = random.randint(1, 10)
        b[linhas1].append(valores2)

somaMatrizes(a, b)
