# IMPORTAÇÕES  ###############################################################################

import nomeDaBiblioteca
import nomeDaBiblioteca as n #Para usar como n.função
from graphics import * #Importa tudo da biblioteca sem precisar utilizar o prefixo "graphics"

# LOOPS  #####################################################################################

while (condição):
    ...

for (i in range(5)):
    ...

# CONDIÇÕES  #################################################################################

if(condição):
    ...
else:
    ...

# ENTRADA e PRINT  ###########################################################################

x = int(input("digite o que você quer ler"))

print(str(x) + "seu valor")

# FUNÇÕES  ###################################################################################

def nomeDaFuncao(parametro1, parametro2):
    ...
    return variavelRetornada

def fatorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fatorial(n-1)

# TIPOS DE DADO  ############################################################################# 

x = int(3)
x = float(3.1415)
x = str(2) #Converte em string
X = True 
X = False

# LISTAS e SEUS MÉTODOS#######################################################################

lista = []
lista.append(4) #Adiciona o valor 4
lista.pop(índice) #Remove o valor desse índice
lista.remove(valor) #Remove o 1º caso desse valor
len(lista) #Retorna o tamanho da lista

lista = [0] * 10 #Cria lista de tamanho 10 zerada
del lista[:] #Apaga elementos de uma lista sem exclui-lá
linha.strip() #Remove caracteres especiais no fim da linha
" ".join(lista) #Pega uma lista de strings e concatena em uma string que separa os itens por " "
x = input().split(" ") #Le varios valores na mesma linha do terminal

# DICIONÁRIOS e SEUS MÉTODOS  ################################################################

dicionário = #Cada chave tem um valor, pode ser uma lista {"A":"Alouuu","B":"Batata","C":"Cabeça"} #Dicionário composto por chave e itens
print(dicionário["A"]) #Mostra os elementos daquela chave
dicionário["D"]="Dado" #Adiciona o elemento ao dicionário
dicionário.get("Chave", "Mensagem caso não encontre") #Para buscar um valor pela chave
dicionário.pop("Chave", "Mensagem caso não encontre") #Para apagar um valor

dicionário.keys()
dicionário.values()

dicionário.update(dic2) #Mescla 2 dicionários

# ARQUIVOS  ##################################################################################

arq = open("arquivo.nome","w") #Escreve
arq = open("arquivo.nome","r") #Le
arq = open("arquivo.nome","a") #Escreve no final
arq.close() #Sempre usar no final
arq.write("sequência") #Escreve no arquivo

# COMENTÁRIOS  ###############################################################################

#Se utiliza Hashtag, ou ''' '''
''' bloco de comentário'''


# EXTRAS  ####################################################################################

try:  #Tenta fazer isso
except: #Se der erro, "Except", faz isso
    
break, continue, e pass #Quebra loop, volta pro início do loop, e continua logo na linha abaixo