#encoding=utf-8
import random

def InsertionSort(lista): #Percorre a lista, trazendo os elementos para frente até achar sua posição
	n = len(lista)
	for i in range(1,n):
		for j in range(i,0,-1):
			if (lista[j-1]>lista[j]):
				lista[j-1], lista[j] = lista[j], lista[j-1]
	return lista

def SelectionSort(lista): #Seleciona o menor e passa para frente
	n = len(lista)
	for j in range(n):
		menorPosicao = j
		for i in range(j, n):
			if (lista[i]<lista[menorPosicao]):
				menorPosicao=i
		lista[j], lista[menorPosicao] = lista[menorPosicao], lista[j]
	return lista

def BubbleSort(lista): #Empurra os elementos para trás
	n = len(lista)
	for j in range(n-1):
		for i in range(n-1):
			if (lista[i]>lista[i+1]):
				lista[i], lista[i+1] = lista[i+1], lista[i]
	return lista


def MergeSort(lista, inicio=0, fim=None): #Divide o problema e vai comparando na volta
	def Merge(lista, inicio, meio, fim):
		esquerda = lista[inicio:meio]
		direita = lista[meio:fim]
		topEsq , topDir = 0 , 0
		for i in range(inicio,fim):
			if (topEsq >= len(esquerda)):
				lista[i]=direita[topDir]
				topDir+=1
			elif (topDir >= len(direita)):
				lista[i]=esquerda[topEsq]
				topEsq+=1
			elif (esquerda[topEsq] < direita[topDir]):
				lista[i]=esquerda[topEsq]
				topEsq+=1
			else:
				lista[i]=direita[topDir]
				topDir+=1

	if (fim==None):
		fim=len(lista)

	if (fim-inicio>1):
		meio = (fim + inicio) //2
		MergeSort(lista, inicio, meio)
		MergeSort(lista, meio, fim)
		Merge(lista, inicio, meio, fim)
	return lista

def QuickSort(lista,inicio=0,fim=None): #Sempre escolhe um pivo e coloca os maiores para direita e menores para esquerda
	def Partition(lista, inicio, fim):
		pivo = lista[fim]
		i = inicio
		for j in range(inicio, fim):
			if (lista[j]<= pivo):
				lista[i], lista[j] = lista[j], lista[i]
				i+=1
		lista[i], lista[fim] = lista[fim], lista[i]
		return i

	if (fim==None):
		fim = len(lista)-1

	if (inicio < fim):
		pivo = Partition(lista, inicio, fim)
		QuickSort(lista, inicio, pivo-1)
		QuickSort(lista, pivo+1, fim)
	return lista


def CountingSort(lista): #Conta quantas vezes cada elemento aparece
	n = len(lista)
	maior=lista[0]
	for i in lista[1:n:1]: #Verifica qual o maior elemento para criar os contadores
		if (i>maior):
			maior=i
	contadores = [0] * (maior+1) 
	for i in lista[0:n:1]: #Conta quantas vezes cada elemento aparece
		contadores[i]+=1
	del lista[:]
	for i in range(len(contadores)): #Efetua a montagem do resultado
		for j in range(contadores[i]):
			lista.append(i) 
	return lista

######## Como escolher ########
#1 - InsertionSort -> n<=2000
	#2 - CountingSort -> nElementos + valorDoMaiorElemento < 2.000.000, inteiros
		#3 - QuickSort -> n<100.000

#range 4 = (1,2,3]
n = 3000
lista = list(range(n))
random.shuffle(lista)

#print(lista)

#lista = InsertionSort(lista)
#lista = SelectionSort(lista)
#lista = BubbleSort(lista)

#lista = MergeSort(lista)
lista = QuickSort(lista)

#lista = CountingSort(lista)

#print("\n"+str(lista))