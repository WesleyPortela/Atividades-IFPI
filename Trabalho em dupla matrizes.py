import random

x = int(input('Digite um valor escalar: '))
n = int(input('Sua matriz quadrada terá quantas linhas e colunas?: '))

a = []
b = []
c = []

contador = 0

for linhas in range(0, n):
    a.append([])
    for colunas in range(0, n):
        valores2 = random.randint(1, 10)
        a[linhas].append(valores2)
        if linhas == colunas:
            if valores2 % 2 == 0:
                contador = contador + 0
            else:
                contador = contador + valores2
print('A operação com a matriz:')
for ja in range(0, n):
    print('{} ' .format(a[ja], end=''))

for linhas1 in range(0, n):
    b.append([])
    for colunas1 in range(0, n):
        valores2 = random.randint(1, 10)
        b[linhas1].append(valores2)

print('Junto da matriz:')
for j in range(0, n):
    print('{} ' .format(b[j], end=''))

result_a = []
result_b = []
for r in range(0, n):
    result_a.append([])
    result_b.append([])
    if contador == 0:
        contador = 1
    else:
        for res in range(0, n):
            result_b[r].append(contador*b[r][res])
            result_a[r].append(x*a[r][res])

print('Resulta na matriz:')
for saida in range(0, n):
    c.append([0]*n)
    for sa in range(0, n):
        c[saida][sa] = result_b[saida][sa] + result_a[saida][sa]
    print(c[saida])
print('-'*30, '\nSendo P(A)= {}\nE sendo X = {}' .format(contador, x))
