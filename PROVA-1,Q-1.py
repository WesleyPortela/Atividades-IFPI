#listas que receberão os nomes e sobrenomes
nome = []
sobrenome = []

n = int(input('Digite a quantidade de nomes compostos: '))
x = 'Nomes separados' #Variavel que guardará temporariamente os nomes divididos

for i in range(1, n+1): #repetição que acontecerá de acordo com a quantidade de nomes compostos escolhidos
    casos = input('Digite o {}º nome composto: ' .format(i)).title()
    x = casos.split(' ', 2)  #Divide o nome digitado pelo usúario
    nome.append(x[0]) #Guarda o 1º nome na lista
    sobrenome.append(x[1]) #Guarda o sobrenome na lista

s_nome = sorted(nome) #variavel que receberá os nomes em ordem alfabética
s_sobrenome = sorted(sobrenome) #variavel que receberá os sobrenomes em ordem alfabética

for r in range(0, n): #repetição que acontecerá de acordo com a quantidade de nomes compostos escolhidos
    print('{} {}' .format(s_nome[r], s_sobrenome[r])) #Saída que mostra o nome e sobrenome de acordo com a posição de (r)
