#encoding=utf-8

def BuscaBinaria(vetor, valor, left=0, right=None):
    if(right==None):
        right = len(vetor)-1
    if(right>=left):
        indice = left + (right-left)//2
        if(vetor[indice]==valor):
            return [valor, indice]
        if(vetor[indice]>valor):
            return BuscaBinaria(vetor, valor, left, indice-1)
        else:
            return BuscaBinaria(vetor, valor, indice+1, right)
    return [None, None]

tamanhoVetor = 1000

vetor = list(range(tamanhoVetor))
valor = int(input("Escolha um valor de busca: "))

print("Valor: " + str(BuscaBinaria(vetor, valor)[0]))
print("Índice: " + str(BuscaBinaria(vetor, valor)[1]))