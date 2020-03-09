n = int(input())
k = int(input())
listaOrdenada = [0] * 1001
indiceAtual = 1000
contaAprovados = 0

for i in range(n): #Conta os casos
    valorAtual = int(input())
    listaOrdenada[valorAtual]+=1

while(indiceAtual>=0): #Verifica quantos foram aprovados
    contaAprovados+=listaOrdenada[indiceAtual]
    if (contaAprovados>= k):
        break
    indiceAtual-=1

print(contaAprovados)