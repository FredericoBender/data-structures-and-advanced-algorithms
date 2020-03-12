tamanhoVetor = 1000000
vetor = list(range(tamanhoVetor+1))

left = 0
right = len(vetor) - 1

iteracoes = 1

def BuscaBinaria(vetor, left, right, valor, iteracoes):
    if(right>=left):
        indice = int(left + (right-left)/2)
        if(vetor[indice]==valor):
            return valor, iteracoes
        if(vetor[indice]>valor):
            return BuscaBinaria(vetor, left, indice-1, valor,iteracoes+1)
        #if(vetor[indice]<valor):
        return BuscaBinaria(vetor, indice+1, right, valor,iteracoes+1)
    return "Não existe",iteracoes

valor = int(input("Escolha um valor de busca: "))
print(BuscaBinaria(vetor, left, right, valor, iteracoes))